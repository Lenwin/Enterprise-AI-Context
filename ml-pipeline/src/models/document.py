from datetime import datetime
from typing import Any
from pydantic import BaseModel,Field

class EnterpriseDocument(BaseModel):
    id:str
    title:str
    content:str
    source:str

    document_type:str="unknown"
    department:str="unknown"
    author:str|None=None
    created_at:datetime|None=None
    updated_at:datetime|None=None
    
    tags:list[str] = Field(default_factory=list)

    metadata:dict[str,Any] = Field(default_factory=list)

    ingested_at:datetime = Field(default_factory=datetime.utcnow)

    @property
    def word_count(self)->int:
        return len(self.content.split())
    @property
    def character_count(self)->int:
        return len(self.content)
    
doc = EnterpriseDocument(
    id="123",
    title="Leave Policy",
    content="Employees receive 20 annual leave days.",
    source="SharePoint"
)

print(doc.model_dump())