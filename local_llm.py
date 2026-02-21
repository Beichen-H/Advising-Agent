from transformers import pipeline
import torch

class LocalLLMClient:
    def __init__(self):
        print("Loading local model...")
        self.generator = pipeline('text-generation', 
                                 model='microsoft/DialoGPT-small')
        self.load_handbook()
    
    def load_handbook(self):
        try:
            with open("data/handbooks/sociology_handbook.txt", "r") as f:
                self.handbook_content = f.read()
        except:
            self.handbook_content = ""
    
    def generate_response(self, messages, **kwargs):
        user_message = ""
        for msg in reversed(messages):
            if msg["role"] == "user":
                user_message = msg["content"]
                break
        
        prompt = f"""Based on this sociology handbook:
        {self.handbook_content[:500]}
        
        Question: {user_message}
        
        Answer:"""
        response = self.generator(prompt, 
                                 max_length=200,
                                 num_return_sequences=1)[0]['generated_text']
        
        return response
