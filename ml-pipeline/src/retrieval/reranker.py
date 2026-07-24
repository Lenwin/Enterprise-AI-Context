from sentence_transformers import CrossEncoder
from src.models.search_result import SearchResult

class CrossEncoderReranker:

    def __init__(self,model_name:str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name)

    def rerank(self,query:str,results:list[SearchResult],top_k:int=5)->list[SearchResult]:
        if not results:
            return []
        pairs = [
            (query,result.content)
            for result in results
        ]

        scores = self.model.predict(pairs)

        for result,score in zip(results,scores):
            result.score = float(score)

        results.sort(
            key=lambda x:x.score,
            reverse = True
        )
        return results[:top_k]