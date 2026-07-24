from pydantic import BaseModel

from src.models.search_result import SearchResult

class RAGResponse(BaseModel):
    answer:str
    sources:list[SearchResult]