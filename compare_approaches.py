import time
from llm_client_openai import OpenAIClient
from rag_client import RAGClient

def compare_approaches():
    print("RAG vs OpenAI")
    print("=" * 80)
    
    # 初始化两个客户端
    old_client = OpenAIClient()
    new_client = RAGClient()
    
    test_questions = [
        "What are the prerequisites for SOC 380?",
        "Can I take STAT 100 instead of SOC 280?",
        "How many hours for Statistics major?",
        "What's the difference between SOC 450 and SOC 495?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n📝 Comparison Test {i}: {question}")
        print("-" * 60)
        
        print("🟡 Old method(All data):")
        start_old = time.time()
        old_response = old_client.generate_response([
            {"role": "user", "content": question}
        ])
        old_time = time.time() - start_old
        print(f"  Respond: {old_response[:150]}...")
        print(f"  Total Time: {old_time:.2f}秒")
        
        print("\n🟢 New Method (RAG):")
        start_new = time.time()
        new_response = new_client.generate_response([
            {"role": "user", "content": question}
        ])
        new_time = time.time() - start_new
        print(f"  响应: {new_response[:150]}...")
        print(f"  时间: {new_time:.2f}秒")
        
        print(f"\n📊 对比: 新方法 {('更快' if new_time < old_time else '更慢')} "
              f"({abs(new_time-old_time):.2f}秒差异)")
        print("-" * 60)

if __name__ == "__main__":
    compare_approaches()
