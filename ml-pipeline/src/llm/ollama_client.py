import time
import ollama
from src.llm.client import BaseLLMClient
from src.llm.response import LLMResponse

class OllamaClient(BaseLLMClient):

    def __init__(self,model_name:str="qwen3:4b"):
        self.model_name = model_name

    def generate(self, prompt)->LLMResponse:

        start = time.perf_counter()

        response=ollama.chat(model=self.model_name,messages=[{"role":"user","content":prompt}])

        latency = (time.perf_counter()-start)*1000

        message = response["message"]["content"]

        prompt_tokens = response.get("prompt_eval_count",0)

        completion_tokens = response.get("eval_count",0)

        return LLMResponse(
            answer=message,
            model_name=self.model_name,
            prompt_tokens = prompt_tokens,
            completion_tokens = completion_tokens,
            total_tokens = prompt_tokens+completion_tokens,
            latency_ms = latency
        )