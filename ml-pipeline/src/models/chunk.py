from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

class DocumentChunk(BaseModel):
    chunk_id:str
    document_id:str
    chunk_index:int
    content:str
    source:str

    metadata: dict[str,Any] = Field(default_factory=dict)
    created_at:datetime = Field(default_factory=datetime.utcnow)

    @property
    def word_count(self)->int:
        return len(self.content.split())
    
    @property

    def character_count(self) -> int:
        return len(self.content)
    