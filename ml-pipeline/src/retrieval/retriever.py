from src.embeddings.embedder import EnterpriseEmbedder
from src.models.search_result import SearchResult
from src.retrieval.query import RetrievalQuery
from src.vectorstore.qdrant_store import EnterpriseQdrantStore

class EnterpriseRetriever:

    def __init__(self,store:EnterpriseQdrantStore):
        self.store = store
        self.embedder = EnterpriseEmbedder()
    def retrieve(self,request:RetrievalQuery)->list[SearchResult]:
        query_embedding = self.embedder.embed_query(request.query)
        return self.store.search(query_embedding=query_embedding,limit=request.top_k,filters=request.filters)

    def embed_text(self,text:str)->list[float]:
        embedding = self.model.encode(text,normalize_embeddings=True)
        return embedding.tolist()
    