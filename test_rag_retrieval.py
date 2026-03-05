from rag_client import RAGClient

def test_retrieval_quality():
    """测试检索质量 - 检查是否找到正确的文档"""
    print("🔍 测试 2: 检索质量测试")
    print("=" * 80)
    
    client = RAGClient()
    
    test_cases = [
        {
            "question": "STAT 410 prerequisites",
            "expected_keywords": ["MATH 241", "STAT 400"],
            "expected_sources": ["statistics"]
        },
        {
            "question": "Sociology major hours",
            "expected_keywords": ["32 hours", "SOC 100", "SOC 280"],
            "expected_sources": ["sociology_major"]
        },
        {
            "question": "Data Science minor requirements",
            "expected_keywords": ["STAT 107", "CS 307", "21 hours"],
            "expected_sources": ["data_science_minor"]
        },
        {
            "question": "Can I take STAT 100 instead of SOC 280?",
            "expected_keywords": ["STAT 100", "SOC 280", "statistics requirement"],
            "expected_sources": ["sociology", "statistics"]
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n📝 测试用例 {i}: {test['question']}")
        print("-" * 60)
        
        # 执行检索（不生成回答）
        print("🔎 检索到的相关文档块:")
        results = client.similarity_search(test['question'], k=3)
        
        # 检查是否包含预期关键词
        all_content = ""
        for doc, score in results:
            all_content += doc.page_content + " "
            print(f"  得分: {score:.4f}")
            print(f"  来源: {doc.metadata.get('source', 'Unknown')}")
            print(f"  预览: {doc.page_content[:150]}...")
            print()
        
        # 评估检索质量
        keywords_found = 0
        for keyword in test['expected_keywords']:
            if keyword.lower() in all_content.lower():
                keywords_found += 1
                print(f"✅ 找到关键词: {keyword}")
            else:
                print(f"❌ 未找到关键词: {keyword}")
        
        accuracy = (keywords_found / len(test['expected_keywords'])) * 100
        print(f"\n📊 检索准确率: {accuracy:.1f}%")
        print("=" * 60)

if __name__ == "__main__":
    test_retrieval_quality()
