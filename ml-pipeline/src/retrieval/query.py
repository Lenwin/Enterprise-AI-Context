from typing import Any
from pydantic import BaseModel,Field

class RetrievalQuery(BaseModel):
    query:str
    top_k:int=5
    filters:dict[str,Any] = Field(default_factory =dict)