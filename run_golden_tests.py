import json
from llm_client_openai import OpenAIClient

def run_golden_dataset_tests():
    """Run tests using the golden dataset"""
    
    # 加载 golden dataset - 使用 utf-8-sig 来处理可能的 BOM
    with open('golden_dataset.json', 'r', encoding='utf-8-sig') as f:
        test_cases = json.load(f)
    
    print("=" * 80)
    print("GOLDEN DATASET TESTING")
    print("=" * 80)
    
    client = OpenAIClient()
    results = []
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test['id']} - {test['department']} - {test['question_type']}")
        print("-" * 60)
        print(f"Q: {test['question']}")
        print(f"Expected: {test['ground_truth'][:100]}...")
        
        # 获取 AI 回答
        response = client.generate_response([
            {"role": "user", "content": test['question']}
        ])
        
        print(f"AI: {response[:200]}...")
        
        # 记录结果
        results.append({
            "id": test['id'],
            "question": test['question'],
            "expected": test['ground_truth'],
            "actual": response,
            "passed": "need manual check"
        })
        
        print("-" * 60)
    
    # 保存结果
    with open('test_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ 测试完成！结果保存到 test_results.json")
    print(f"共测试 {len(test_cases)} 个问题")

if __name__ == "__main__":
    run_golden_dataset_tests()
