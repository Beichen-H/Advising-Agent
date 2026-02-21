import os
from pathlib import Path

def setup_environment():
    """Setup the environment and create necessary directories"""
    directories = [
        "data/handbooks",
        "data/vector_store",
        "data/surveys",
        "logs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {directory}")
    
    print("\n📁 Environment setup complete!")

def check_api_key():
    """Test the API key"""
    try:
        from openai import OpenAI
        client = OpenAI(
            api_key="uc_027d1aafe600416c8ae762cc7dc3bcaf",
            base_url="https://chat.api.uiuc.edu/v1"
        )
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'API key is working'"}],
            max_tokens=20
        )
        
        print("✅ API key is working!")
        return True
    except Exception as e:
        print(f"❌ API key test failed: {e}")
        return False

if __name__ == "__main__":
    print("🎓 LAS Academic Advising Assistant - Setup\n")
    setup_environment()
    
    print("\n" + "="*50)
    print("\nTesting API connection...")
    check_api_key()
    
    print("\n" + "="*50)
    print("\n✅ Setup complete!")
