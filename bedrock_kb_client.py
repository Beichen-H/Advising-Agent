import os
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = "us-east-1"
BEDROCK_KNOWLEDGE_BASE_ID = "9T3ZW2COOC"
BEDROCK_MODEL_ARN = "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-lite-v1:0"


class BedrockKnowledgeBaseClient:
    def __init__(self):
        self.region = os.getenv("AWS_REGION", "us-east-1")
        self.knowledge_base_id = os.getenv("BEDROCK_KNOWLEDGE_BASE_ID")
        self.model_arn = os.getenv("BEDROCK_MODEL_ARN")

        if not self.knowledge_base_id:
            raise ValueError("Missing BEDROCK_KNOWLEDGE_BASE_ID")
        if not self.model_arn:
            raise ValueError("Missing BEDROCK_MODEL_ARN")

        self.client = boto3.client(
            "bedrock-agent-runtime",
            region_name=self.region
        )

    def answer_question(self, query: str, session_id: str | None = None) -> dict:
        try:
            request = {
                "input": {"text": query},
                "retrieveAndGenerateConfiguration": {
                    "type": "KNOWLEDGE_BASE",
                    "knowledgeBaseConfiguration": {
                        "knowledgeBaseId": self.knowledge_base_id,
                        "modelArn": self.model_arn,
                        "retrievalConfiguration": {
                            "vectorSearchConfiguration": {
                                "numberOfResults": 5
                            }
                        }
                    }
                }
            }

            if session_id:
                request["sessionId"] = session_id

            response = self.client.retrieve_and_generate(**request)
            return response

        except ClientError as e:
            raise RuntimeError(f"Bedrock error: {e}") from e
