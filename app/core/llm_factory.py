from langchain_ollama import ChatOllama
from app.core.config import settings

class LLMFactory:
    @staticmethod
    def ollama_cloud():
        return ChatOllama(
            model=settings.OLLAMA_COMPLETIONS_MODEL,
            api_key=settings.OLLAMA_API_KEY,
            base_url="https://api.ollama.com",
            temperature=0.7,
        )

    @staticmethod
    def ollama_local():
        return ChatOllama(
            model=settings.OLLAMA_COMPLETIONS_MODEL,
            api_key=settings.OLLAMA_API_KEY,
            base_url="http://localhost:11434",
            temperature=0.7,
        )