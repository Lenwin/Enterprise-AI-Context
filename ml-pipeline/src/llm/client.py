from abc import ABC, abstractmethod

from src.llm.response import LLMResponse

class BaseLLMClient(ABC):
    @abstractmethod
    def generate(self,prompt:str)->LLMResponse:
        pass
    