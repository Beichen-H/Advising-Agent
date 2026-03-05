from rag_client import RAGClient
import re

class HybridRAGClient(RAGClient):
    def __init__(self):
        super().__init__()
    
    def keyword_search(self, query, k=5):
        """简单的关键字搜索作为补充"""
        keywords = re.findall(r'\b[A-Z]{3,4}\s+\d{3}\b', query)  # 提取课程代码
        keywords.extend(re.findall(r'\b\d+\s*hours?\b', query.lower()))  # 提取小时数
        
        results = []
        if keywords:
            # 在所有文档中搜索关键词
            all_docs = self.vectorstore.get()
            for i, doc in enumerate(all_docs['documents']):
                score = 0
                for kw in keywords:
                    if kw.lower() in doc.lower():
                        score += 1
                if score > 0:
                    results.append((doc, score / len(keywords)))
        
        return sorted(results, key=lambda x: x[1], reverse=True)[:k]
    
    def generate_response(self, messages, **kwargs):
        user_message = ""
        for msg in reversed(messages):
            if msg["role"] == "user":
                user_message = msg["content"]
                break
        
        # 混合检索：向量检索 + 关键词检索
        vector_results = self.vectorstore.similarity_search_with_score(user_message, k=5)
        keyword_results = self.keyword_search(user_message, k=3)
        
        # 合并结果
        all_results = []
        seen = set()
        
        for doc, score in vector_results:
            content = doc.page_content[:100]
            if content not in seen:
                all_results.append((doc, score))
                seen.add(content)
        
        print(f"🔍 Found {len(all_results)} unique results")
        
        # 使用合并后的结果
        context = "\n\n".join([doc.page_content for doc, _ in all_results[:5]])
        
        # 构建提示
        prompt = f"""Based on the following information from UIUC handbooks, please answer the question.

Information:
{context}

Question: {user_message}

Answer based ONLY on the information provided above. If the information doesn't contain the answer, say so."""

        response = self.llm.invoke(prompt)
        
        return response.content
