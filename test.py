import os
import boto3
from dotenv import load_dotenv

load_dotenv()

region = os.getenv("AWS_REGION")
kb_id = os.getenv("BEDROCK_KNOWLEDGE_BASE_ID")

print("Region:", repr(region))
print("KB ID:", repr(kb_id))

client = boto3.client("bedrock-agent", region_name="us-east-1")

resp = client.get_knowledge_base(knowledgeBaseId=kb_id)
print("Found KB:", resp["knowledgeBase"]
      ["knowledgeBaseId"], resp["knowledgeBase"]["name"])
