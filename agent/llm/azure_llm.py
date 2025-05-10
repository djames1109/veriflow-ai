import os

from langchain_openai import AzureChatOpenAI


class AzureLLM:

    def __init__(self):
        self.azure_openai_api_key = os.getenv("AZURE_API_KEY")
        self.azure_openai_endpoint = os.getenv("AZURE_ENDPOINT")
        self.azure_model_version = os.getenv("AZURE_MODEL_VERSION")
        self.azure_deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")
        self.azure_api_version = os.getenv("AZURE_API_VERSION")
        if not self.azure_openai_api_key or not self.azure_openai_endpoint:
            raise ValueError("Azure API key or endpoint not found.")

    def initiate(self):
        return AzureChatOpenAI(
            model_version=self.azure_model_version,
            api_key=self.azure_openai_api_key,
            azure_endpoint=self.azure_openai_endpoint,
            azure_deployment=self.azure_deployment_name,
            api_version=self.azure_api_version)
