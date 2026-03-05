from rag_client import RAGClient

def test_rag():
    print("=" * 60)
    print("🧪 Testing RAG System")
    print("=" * 60)
    
    # 初始化 RAG 客户端
    client = RAGClient()
    
    # 测试问题
    test_questions = [
        "What are the prerequisites for STAT 410?",
        "How many total hours for Sociology major?",
        "Can I take STAT 100 instead of SOC 280?",
        "What's the difference between SOC 450 and SOC 495?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n📝 Test {i}: {question}")
        print("-" * 40)
        
        response = client.generate_response([
            {"role": "user", "content": question}
        ])
        
        print(f"🤖 Response:\n{response}")
        print("=" * 60)

if __name__ == "__main__":
    test_rag()
