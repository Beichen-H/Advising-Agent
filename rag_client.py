import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from config import Config

class RAGClient:
    def __init__(self):
        print("🔄 Initializing RAG system...")
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=Config.OPENAI_API_KEY,
            model="text-embedding-ada-002"
        )
        self.llm = ChatOpenAI(
            openai_api_key=Config.OPENAI_API_KEY,
            model=Config.OPENAI_MODEL,
            temperature=0.1  # 降低温度，提高确定性
        )
        self.vectorstore = None
        self.qa_chain = None
        self.persist_directory = "./data/chroma_db"
        
        self.load_or_create_vectorstore()
    
    def load_or_create_vectorstore(self):
        if os.path.exists(self.persist_directory) and os.listdir(self.persist_directory):
            print("📚 Loading existing vector database...")
            self.vectorstore = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )
        else:
            print("🆕 Creating new vector database...")
            self.create_vectorstore()
        
        # 简化：使用最基本的检索
        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 8}  # 增加检索数量
        )
        
        # 改用简单的 stuff 链（更快）
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",  # 改回 stuff，更快
            retriever=self.retriever,
            return_source_documents=True,
            verbose=False  # 关闭详细输出，提高速度
        )
        print("✅ RAG system ready!")
    
    def create_vectorstore(self):
        loader = DirectoryLoader(
            "data/knowledge_base/",
            glob="**/*.txt",
            loader_cls=TextLoader,
            loader_kwargs={'encoding': 'utf-8'}
        )
        documents = loader.load()
        print(f"📄 Loaded {len(documents)} documents")
        
        # 优化分块：针对课程代码和数字
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=["\n\n", "\n", ". ", "! ", "? ", " ", ""]
        )
        chunks = text_splitter.split_documents(documents)
        print(f"✂️  Split into {len(chunks)} chunks")
        
        # 添加课程代码作为关键词
        import re
        for chunk in chunks:
            # 提取课程代码作为元数据
            course_codes = re.findall(r'[A-Z]{3,4}\s+\d{3}', chunk.page_content)
            if course_codes:
                chunk.metadata['courses'] = ','.join(course_codes)
            
            # 提取数字信息
            numbers = re.findall(r'\b\d{2,3}\b', chunk.page_content)
            if numbers:
                chunk.metadata['numbers'] = ','.join(numbers)
        
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        print(f"💾 Vector database saved to {self.persist_directory}")
    
    def generate_response(self, messages, **kwargs):
        user_message = ""
        for msg in reversed(messages):
            if msg["role"] == "user":
                user_message = msg["content"]
                break
        
        print(f"🔍 Searching for: {user_message}")
        
        result = self.qa_chain.invoke({"query": user_message})
        
        # 提取来源
        sources = set()
        for doc in result.get('source_documents', [])[:3]:  # 只取前3个
            source = os.path.basename(doc.metadata.get('source', 'Unknown'))
            sources.add(source)
        
        response = result['result']
        if sources:
            response += f"\n\n📚 **Sources:** {', '.join(sources)}"
        
        return response
