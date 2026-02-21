import requests
import openai
from openai import OpenAI

print("🔍 Testing API Connection...")
print("-" * 50)

try:
    response = requests.get("https://chat.api.uiuc.edu", timeout=5)
    print(f"✅ UIUC Chat domain is reachable (status: {response.status_code})")
except Exception as e:
    print(f"❌ Cannot reach UIUC Chat domain: {e}")

try:
    client = OpenAI(
        api_key="uc_027d1aafe600416c8ae762cc7dc3bcaf",
        base_url="https://chat.api.uiuc.edu/v1",
        timeout=10
    )
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say 'Hello'"}],
        max_tokens=10
    )
    print(f"✅ API connection successful!")
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"❌ API connection failed: {type(e).__name__}: {e}")

print("\n🔄 Testing alternative endpoints...")
endpoints = [
    "https://chat.api.uiuc.edu/v1",
    "https://uiuc.chat/v1",
    "https://api.uiuc.chat/v1"
]

for endpoint in endpoints:
    try:
        client = OpenAI(
            api_key="uc_027d1aafe600416c8ae762cc7dc3bcaf",
            base_url=endpoint,
            timeout=5
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hi"}],
            max_tokens=5
        )
        print(f"✅ Endpoint {endpoint} works!")
        break
    except Exception as e:
        print(f"❌ Endpoint {endpoint} failed: {type(e).__name__}")

print("-" * 50)
