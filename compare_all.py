from llm_client_openai import OpenAIClient
from rag_client import RAGClient
from custom_retriever import CustomRAGClient
import json
import time

def compare_all():
    """对比所有方法"""
    
    with open('golden_dataset.json', 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
    
    clients = {
        'old': OpenAIClient(),
        'rag': RAGClient(),
        'custom': CustomRAGClient()
    }
    
    results = {name: {'correct': 0, 'time': 0} for name in clients}
    
    for i, test in enumerate(test_cases[:5]):  # 先测试5个
        print(f"\n📝 Test {i+1}: {test['id']}")
        
        for name, client in clients.items():
            start = time.time()
            response = client.generate_response([{"role": "user", "content": test['question']}])
            elapsed = time.time() - start
            
            # 简单评估
            ground_truth = test['ground_truth'].lower()
            response_lower = response.lower()
            
            # 检查关键信息
            key_phrases = ground_truth.split('.')[0].split()[:3]
            correct = all(phrase in response_lower for phrase in key_phrases)
            
            if correct:
                results[name]['correct'] += 1
            results[name]['time'] += elapsed
            
            print(f"  {name}: {'✅' if correct else '❌'} ({elapsed:.2f}s)")
    
    print("\n" + "="*60)
    print("📊 对比结果")
    print("="*60)
    for name, stats in results.items():
        print(f"\n{name}:")
        print(f"  准确率: {stats['correct']}/5")
        print(f"  平均时间: {stats['time']/5:.2f}s")

if __name__ == "__main__":
    compare_all()
