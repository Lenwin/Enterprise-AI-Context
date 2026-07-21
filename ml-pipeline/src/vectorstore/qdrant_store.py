from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance,VectorParams
from qdrant_client.models import PointStruct
from src.models.embedding import EmbeddingRecord
import uuid
from qdrant_client.models import Filter
from src.models.search_result import SearchResult

class EnterpriseQdrantStore:

    DEFAULT_COLLECTION = "enterprise_documents"

    def __init__(self,embedding_dimension:int,host:str = "localhost",port:int = 6333,collection_name:str = DEFAULT_COLLECTION,in_memory:bool = False):
        self.embedding_dimension = embedding_dimension
        self.collection_name = collection_name
        if in_memory:
            self.client = QdrantClient(":memory:")
        else:
            self.client = QdrantClient(host=host,port=port)
    
    def create_collection(self):
        if self.collection_exists():
            return 
        
        self.client.create_collection(
            collection_name = self.collection_name,
            vectors_config = VectorParams(
                size = self.embedding_dimension,
                distance=Distance.COSINE
            )
        )
    
    def collection_exists(self) ->bool:
        
        collections = self.client.get_collections()

        return any(
            collection.name == self.collection_name
            for collection in collections.collections
        )
    def count(self) ->int:

        if not self.collection_exists():
            return 0
        
        response = self.client.count(
            collection_name=self.collection_name
        )
        return response.count
    
    def delete_collection(self):

        if self.collection_exists():
            self.client.delete_collection(self.collection_name)

    def upsert(self,records: list[EmbeddingRecord])->None:
        if not self.collection_exists():
            self.create_collection()
        
        points = []

        for record in records:
            point_id = str(uuid.uuid5(
                uuid.NAMESPACE_DNS,record.chunk_id
            ))
            points.append(PointStruct(id=point_id,vector = record.embedding,
                                      payload={"chunk_id": record.chunk_id,
                                                "document_id": record.document_id,
                                                "content": record.content,
                                                "source": record.source,
                                                **record.metadata
                                            }
                                    )
                        )

        result = self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

        print(result)

    def search(self,query_embedding:list[float],limit: int = 5)->list[SearchResult]:
        results = self.client.query_points(
            collection_name = self.collection_name,
            query = query_embedding,
            limit = limit,
        ).points
        search_results:list[SearchResult] = []

        for point in results:

            payload = point.payload

            metadata = {
                key:value
                for key,value in payload.items()
                if key not in{
                    "chunk_id",
                    "document_id",
                    "content",
                    "source",
                }
            }
            search_results.append(
                SearchResult(
                    chunk_id=payload["chunk_id"],
                    document_id = payload["document_id"],
                    score = point.score,
                    content=payload["content"],
                    source = payload["source"],
                    metadata = metadata
                )
            )
            return search_results