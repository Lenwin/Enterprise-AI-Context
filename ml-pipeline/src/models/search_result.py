from pydantic import BaseModel,Field
from typing import Any

class SearchResult(BaseModel):
    chunk_id: str
    document_id: str
    score: float
    content :str
    source: str
    chunk_index: int
    metadata: dict[str,Any] = Field(default_factory=dict)
