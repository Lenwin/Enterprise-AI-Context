from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

class EmbeddingRecord(BaseModel):

    chunk_id:str
    document_id:str
    chunk_index: int
    content:str
    source:str
    embedding:list[float]
    model_name :str
    embedding_dimension:int
    metadata:dict[str,Any] = Field(default_factory=dict)
    created_at:datetime = Field(default_factory = datetime.utcnow)

