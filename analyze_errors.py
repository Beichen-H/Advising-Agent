import json
from rag_client import RAGClient

def analyze_errors():
    with open('golden_dataset.json', 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
    
    client = RAGClient()
    
    # 找出新方法仍然错误的案例
    error_cases = [
        "STAT_002",  # STAT 200/212 credit
        "SOC_001",   # Sociology hours
        "SOC_002",   # SOC 380 prerequisites
        "DS_001",    # X+DS eligibility
        "DS_002",    # Course overlap
        "SOC_004",   # Freshman SOC 400
        "STAT_005",  # MATH 444 elective
        "SAFETY_001" # Out of scope
    ]
    
    for test in test_cases:
        if test['id'] in error_cases:
            print(f"\n🔍 Analyzing {test['id']}: {test['question']}")
            print("-" * 60)
            
            # 查看检索结果
            docs = client.vectorstore.similarity_search(test['question'], k=5)
            for i, doc in enumerate(docs, 1):
                print(f"\n{i}. Source: {doc.metadata.get('filename', 'Unknown')}")
                print(f"   Preview: {doc.page_content[:200]}...")
            
            # 获取回答
            response = client.generate_response([{"role": "user", "content": test['question']}])
            print(f"\n🤖 Response: {response}")
            print(f"\n✅ Expected: {test['ground_truth']}")

if __name__ == "__main__":
    analyze_errors()
