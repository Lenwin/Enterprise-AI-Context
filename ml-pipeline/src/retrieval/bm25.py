from rank_bm25 import BM25Okapi

from src.models.chunk import DocumentChunk
from src.models.search_result import SearchResult

class BM25Retriever:

    def __init__(self):
        self.chunks:list[DocumentChunk] = []
        self.bm25: BM250kapi| None=None

    def index(self,chunks:list[DocumentChunk])->None:
        self.chunks = chunks
        corpus = [
            chunk.content.lower().split()
            for chunk in chunks
        ]
        self.bm25 = BM25Okapi(corpus)

    def search(self,query:str,top_k:int=5)->list[SearchResult]:
        if self.bm25 is None:
            return []

        query_tokens = query.lower().split()
        scores = self.bm25.get_scores(query_tokens)

        ranked = sorted(enumerate(scores),key=lambda x:x[1],reverse=True)[:top_k]

        results = []

        for index,score in ranked:

            chunk = self.chunks[index]
            results.append(
                SearchResult(
                    chunk_id=chunk.chunk_id,
                    document_id = chunk.document_id,
                    chunk_index = chunk.chunk_index,
                    score = float(score),
                    content = chunk.content,
                    source = chunk.source,
                    metadata = chunk.metadata
                )
            )
        return results