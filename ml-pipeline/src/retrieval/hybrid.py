from src.models.search_result import SearchResult
from src.retrieval.bm25 import BM25Retriever
from src.retrieval.query import RetrievalQuery
from src.retrieval.retriever import EnterpriseRetriever

from collections import defaultdict

class HybridRetriever:
    def __init__(self,vector_retriever:EnterpriseRetriever,bm25_retriever:BM25Retriever,rrf_k:int=60):
        self.vector = vector_retriever
        self.bm25 = bm25_retriever
        self.rrf_k = rrf_k

    def retrieve(self,request:RetrievalQuery)->list[SearchResult]:

        vector_results = self.vector.retrieve(request)

        bm25_results = self.bm25.search(request.query,request.top_k)
        scores = defaultdict(float)
        lookup = {}


        for rank,result in enumerate(vector_results):
            scores[result.chunk_id] += 1/(self.rrf_k+rank+1)
            lookup[result.chunk_id] = result

        for rank,result in enumerate(bm25_results):
            scores[result.chunk_id] += 1/(self.rrf_k+rank+1)
            if result.chunk_id not in lookup:
                lookup[result.chunk_id] = result

        ranked = sorted(scores.items(),key=lambda x:x[1],reverse=True)
        final_results = []

        for chunk_id,fused_score in ranked[: request.top_k]:
            result = lookup[chunk_id]
            result.score = fused_score
            final_results.append(result)

        return final_results