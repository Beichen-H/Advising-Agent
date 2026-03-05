import os
import re
from rag_client import RAGClient

class CustomRAGClient(RAGClient):
    def __init__(self):
        super().__init__()
    
    def extract_key_info(self, query):
        """提取查询中的关键信息"""
        info = {
            'course_codes': re.findall(r'[A-Z]{3,4}\s+\d{3}', query.upper()),
            'numbers': re.findall(r'\b\d{2,3}\b', query),
            'keywords': []
        }
        
        # 特定关键词
        if 'prerequisite' in query.lower():
            info['keywords'].append('prerequisite')
        if 'credit' in query.lower():
            info['keywords'].append('credit')
        if 'hours' in query.lower():
            info['keywords'].append('hours')
        
        return info
    
    def custom_search(self, query, k=10):
        """自定义搜索，结合向量和关键词"""
        # 向量搜索
        vector_results = self.vectorstore.similarity_search_with_score(query, k=k)
        
        # 提取关键信息
        key_info = self.extract_key_info(query)
        
        # 重新排序
        scored_results = []
        for doc, score in vector_results:
            new_score = score
            content = doc.page_content.lower()
            
            # 如果包含查询中的课程代码，加分
            for code in key_info['course_codes']:
                if code.lower() in content:
                    new_score -= 0.1  # 分数越低越好
            
            # 如果包含查询中的数字，加分
            for num in key_info['numbers']:
                if num in content:
                    new_score -= 0.05
            
            # 如果包含关键词，加分
            for kw in key_info['keywords']:
                if kw in content:
                    new_score -= 0.1
            
            scored_results.append((doc, new_score))
        
        # 按新分数排序
        scored_results.sort(key=lambda x: x[1])
        
        return scored_results[:5]
    
    def generate_response(self, messages, **kwargs):
        user_message = ""
        for msg in reversed(messages):
            if msg["role"] == "user":
                user_message = msg["content"]
                break
        
        print(f"🔍 Custom searching for: {user_message}")
        
        # 使用自定义搜索
        results = self.custom_search(user_message)
        
        # 构建上下文
        context = "\n\n".join([doc.page_content for doc, _ in results])
        
        # 构建提示
        prompt = f"""Based on the following information from UIUC handbooks, please answer the question accurately.

INFORMATION:
{context}

QUESTION: {user_message}

INSTRUCTIONS:
1. Only use information from the provided text
2. If the information is not in the text, say "I cannot find this information in the handbooks"
3. Be specific and accurate about course codes and numbers
4. Include relevant prerequisites or restrictions

ANSWER:"""

        response = self.llm.invoke(prompt)
        
        # 提取来源
        sources = set()
        for doc, _ in results:
            source = os.path.basename(doc.metadata.get('source', 'Unknown'))
            sources.add(source)
        
        result = response.content
        if sources:
            result += f"\n\n📚 **Sources:** {', '.join(sources)}"
        
        return result
