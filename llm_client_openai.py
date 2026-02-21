import openai
from config import Config
import os

class OpenAIClient:
    def __init__(self):
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        self.model = Config.OPENAI_MODEL
        print("✅ Connected to OpenAI API")
        print("📚 Loading knowledge base...")
        self.knowledge_base = self.load_all_knowledge()
        
        self.contacts = {
            "sociology": {
                "name": "Sociology Department",
                "email": "soc-advising@illinois.edu",
                "phone": "(217) 333-1950",
                "office": "3120 Lincoln Hall",
                "website": "https://sociology.illinois.edu"
            },
            "statistics": {
                "name": "Statistics Department",
                "email": "stat-ugrad@illinois.edu",
                "phone": "(217) 333-2167",
                "office": "156 Computing Applications Building",
                "website": "https://stat.illinois.edu"
            },
            "stat_cs": {
                "name": "Statistics & Computer Science Program",
                "email": "stat-ugrad@illinois.edu",
                "phone": "(217) 333-2167",
                "office": "156 Computing Applications Building",
                "website": "https://stat.illinois.edu"
            },
            "data_science": {
                "name": "Data Science Programs",
                "email": "stat-ugrad@illinois.edu",
                "phone": "(217) 333-2167",
                "office": "156 Computing Applications Building",
                "website": "https://stat.illinois.edu"
            },
            "economics": {
                "name": "Economics Department",
                "email": "econ-advising@illinois.edu",
                "phone": "(217) 333-0120",
                "office": "214 David Kinley Hall",
                "website": "https://economics.illinois.edu"
            },
            "psychology": {
                "name": "Psychology Department",
                "email": "psych-advising@illinois.edu",
                "phone": "(217) 333-0631",
                "office": "603 Psychology Building",
                "website": "https://psychology.illinois.edu"
            }
        }

    
    def get_contact_info(self, dept):
        dept = dept.lower()
        if dept in self.contacts:
            info = self.contacts[dept]
            return f"{info['name']}\nEmail: {info['email']}\nPhone: {info['phone']}\nOffice: {info['office']}"
        return None
    
    def get_all_contacts_summary(self):
        summary = "\n\nDEPARTMENT CONTACT INFORMATION (Use when students need to reach a specific department):\n"
        for dept, info in self.contacts.items():
            summary += f"\n{info['name']}:\n"
            summary += f"  Email: {info['email']}\n"
            summary += f"  Phone: {info['phone']}\n"
            summary += f"  Office: {info['office']}\n"
        return summary
    
    def load_all_knowledge(self):
        """Load all knowledge base files from organized folders"""
        base_dir = "data/knowledge_base"
        all_content = []
        
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
            return "No knowledge base found."
        
        for dept_folder in sorted(os.listdir(base_dir)):
            dept_path = os.path.join(base_dir, dept_folder)
            if os.path.isdir(dept_path):
                dept_content = []
                print(f"  📂 Loading {dept_folder}...")
                for filename in sorted(os.listdir(dept_path)):
                    if filename.endswith('.txt'):
                        filepath = os.path.join(dept_path, filename)
                        try:
                            with open(filepath, 'r', encoding='utf-8') as f:
                                content = f.read()
                                dept_content.append(f"\n\n--- {dept_folder}/{filename} ---\n{content}")
                                print(f"    ✅ Loaded: {filename}")
                        except Exception as e:
                            print(f"    ❌ Error loading {filename}: {e}")
                
                if dept_content:
                    header = f"\n\n{'='*60}\nDEPARTMENT: {dept_folder.upper()}\n{'='*60}"
                    all_content.append(header + "".join(dept_content))
        general_path = "data/knowledge_general"
        if os.path.exists(general_path):
            for filename in sorted(os.listdir(general_path)):
                if filename.endswith('.txt'):
                    filepath = os.path.join(general_path, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                            all_content.append(f"\n\n--- GENERAL/{filename} ---\n{content}")
                            print(f"  ✅ Loaded general: {filename}")
                    except Exception as e:
                        print(f"  ❌ Error loading general {filename}: {e}")
        
        if all_content:
            return "\n".join(all_content)
        else:
            print("⚠️ No knowledge base files found")
            return "No knowledge base content available."
    
    def generate_response(self, messages, temperature=0.7, max_tokens=1000):
        """Generate response using OpenAI API with knowledge base context"""
        try:
            user_message = ""
            for msg in reversed(messages):
                if msg["role"] == "user":
                    user_message = msg["content"]
                    break
            
            knowledge = self.knowledge_base
            contacts_info = self.get_all_contacts_summary()
            
            system_prompt = f"""{Config.SYSTEM_PROMPT}

You have access to the following official UIUC department documents:

{knowledge}

{contacts_info}

IMPORTANT GUIDELINES:
1. When answering, always specify which department/program the information comes from.
2. If a question involves multiple departments, synthesize information from all relevant documents.
3. If information is not available in the documents, acknowledge this and provide the appropriate department contact information.
4. Use the contact information naturally in your responses. For example:
   - "For more specific questions about Sociology, you can reach out to soc-advising@illinois.edu"
   - "I don't have that information in my knowledge base. I recommend contacting the Statistics Department at stat-advising@illinois.edu"
5. Be accurate about course codes, prerequisites, and requirements.
6. Always remind students to check the official Course Explorer (https://courses.illinois.edu) for current course offerings and schedules.

Your tone should be helpful, professional, and supportive."""

            api_messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=api_messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"❌ Error calling API: {e}"
