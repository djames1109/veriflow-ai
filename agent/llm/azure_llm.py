import os
import sys

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI


class AzureLLM:

    def __init__(self):
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        load_dotenv()

        self.azure_openai_api_key = os.getenv("AZURE_OPENAI_KEY")
        self.azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.azure_model_version = os.getenv("AZURE_MODEL_VERSION")
        self.azure_deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")
        self.azure_api_version = os.getenv("AZURE_API_VERSION")

        if not self.azure_openai_api_key or not self.azure_openai_endpoint:
            raise ValueError("Azure API key or endpoint not found.")

    def create(self):
        print(f"Using Azure API key: {self.azure_openai_api_key}")
        print(f"Using Azure endpoint: {self.azure_openai_endpoint}")
        print(f"Using Azure deployment: {self.azure_deployment_name}")
        print(f"Using Azure model version: {self.azure_model_version}")
        print(f"Using Azure API version: {self.azure_api_version}")

        return AzureChatOpenAI(
            model_version=self.azure_model_version,
            api_key=self.azure_openai_api_key,
            azure_endpoint=self.azure_openai_endpoint,
            azure_deployment=self.azure_deployment_name,
            api_version=self.azure_api_version)
