from llm_client_openai import OpenAIClient

def test_openai():
    print("🔍 Testing OpenAI Connection...")
    print("-" * 50)
    
    client = OpenAIClient()
    
    test_questions = [
        "What are the Sociology major requirements?",
        "Should I take both SOC 400 and SOC 495?",
        "What's the difference between SOC 280 and SOC 380?"
    ]
    
    for question in test_questions:
        print(f"\n❓ Question: {question}")
        print("-" * 30)
        response = client.generate_response([
            {"role": "user", "content": question}
        ])
        print(f"🤖 Response: {response}")
        print()
    
    print("✅ Test complete!")

if __name__ == "__main__":
    test_openai()
