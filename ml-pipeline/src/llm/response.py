from datetime import datetime
from pydantic import BaseModel,Field

class LLMResponse(BaseModel):
    answer:str
    model_name:str
    prompt_tokens:int =0
    completion_tokens:int=0
    total_tokens: int=0
    latency_ms:float = 0
    created_at:datetime = Field(default_factory=datetime.utcnow)