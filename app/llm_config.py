import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class LLMConfig:
    def __init__(self, provider: str, model: str, api_key: str = None):
        self.provider = provider
        self.model = model
        self.api_key = api_key
        logging.info(f"Initializing LLMConfig: provider={provider}, model={model}")
        if provider == "ollama":
            from langchain_community.llms import Ollama
            self.llm = Ollama(model=model)
            logging.info("Ollama LLM initialized.")
        elif provider == "openai":
            from langchain.chat_models import ChatOpenAI
            self.llm = ChatOpenAI(model=model, api_key=api_key)
            logging.info("OpenAI LLM initialized.")
        else:
            logging.error(f"Unsupported provider: {provider}")
            raise ValueError(f"Unsupported provider: {provider}")

#llm_config = LLMConfig(provider="openai", model="gpt-4.1-nano")
llm_config = LLMConfig(
    provider="openai",
    model="gpt-4.1-nano",
    api_key=os.getenv("OPENAI_API_KEY")
)