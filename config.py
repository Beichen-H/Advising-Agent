import os
from dotenv import load_dotenv

# add API_KEY to .env and load it in for security
load_dotenv()


class Config:
    # OpenAI API Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_KEY")
    OPENAI_MODEL = "gpt-3.5-turbo"

    # System Prompt
    SYSTEM_PROMPT = """You are an academic advising assistant for multiple departments at UIUC.
    You have access to official department documents and contact information.
    Be helpful, accurate, and professional. When information is not available,
    provide the appropriate department contact information naturally in your response."""
