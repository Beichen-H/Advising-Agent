import json
from llm_client_openai import OpenAIClient
from rag_client import RAGClient
import time

def evaluate_accuracy():
    """评估新旧方法的准确率"""
    
    # 加载 golden dataset
    with open('golden_dataset.json', 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
    
    old_client = OpenAIClient()
    new_client = RAGClient()
    
    results = {
        "old_method": {"correct": 0, "total": 0, "time": 0},
        "new_method": {"correct": 0, "total": 0, "time": 0}
    }
    
    for test in test_cases:
        question = test['question']
        ground_truth = test['ground_truth']
        
        print(f"\n📝 Testing: {test['id']}")
        
        # 测试旧方法
        start = time.time()
        old_response = old_client.generate_response([{"role": "user", "content": question}])
        old_time = time.time() - start
        
        # 简单评估（检查是否包含关键信息）
        old_correct = all(kw.lower() in old_response.lower() 
                         for kw in ground_truth.split()[:5])
        
        results['old_method']['total'] += 1
        if old_correct:
            results['old_method']['correct'] += 1
        results['old_method']['time'] += old_time
        
        # 测试新方法
        start = time.time()
        new_response = new_client.generate_response([{"role": "user", "content": question}])
        new_time = time.time() - start
        
        new_correct = all(kw.lower() in new_response.lower() 
                         for kw in ground_truth.split()[:5])
        
        results['new_method']['total'] += 1
        if new_correct:
            results['new_method']['correct'] += 1
        results['new_method']['time'] += new_time
        
        print(f"  旧方法: {'✅' if old_correct else '❌'} ({old_time:.2f}s)")
        print(f"  新方法: {'✅' if new_correct else '❌'} ({new_time:.2f}s)")
    
    # 输出统计
    print("\n" + "="*60)
    print("📊 准确率对比")
    print("="*60)
    
    for method in ['old_method', 'new_method']:
        accuracy = (results[method]['correct'] / results[method]['total']) * 100
        avg_time = results[method]['time'] / results[method]['total']
        print(f"\n{method}:")
        print(f"  准确率: {accuracy:.1f}% ({results[method]['correct']}/{results[method]['total']})")
        print(f"  平均时间: {avg_time:.2f}秒")

if __name__ == "__main__":
    evaluate_accuracy()
