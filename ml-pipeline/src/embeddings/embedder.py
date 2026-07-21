from sentence_transformers import SentenceTransformer

from src.models.chunk import DocumentChunk
from src.models.embedding import EmbeddingRecord

class EnterpriseEmbedder:
    def __init__(self,model_name:str = "BAAI/bge-base-en-v1.5"):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
    def embed_chunk(self,chunk:DocumentChunk)->EmbeddingRecord:
        embedding =self.model.encode(chunk.content,normalize_embeddings=True)

        return EmbeddingRecord(
            chunk_id=chunk.chunk_id,
            document_id=chunk.document_id,
            content=chunk.content,
            source=chunk.source,
            embedding=embedding.tolist(),
            model_name=self.model_name,
            embedding_dimension=len(embedding),
            metadata=chunk.metadata.copy(),
        )
    
    def embed_query(self,query:str)->list[float]:
        embedding = self.model.encode(query,normalize_embeddings=True)
        return embedding.tolist()
    
    def embed_chunks(self,chunks:list[DocumentChunk])->list[EmbeddingRecord]:
        embeddings = self.model.encode(
            [chunk.content for chunk in chunks],
            normalize_embeddings = True
        )
        records:list[EmbeddingRecord] = []

        for chunk,embedding in zip(chunks,embeddings):
            records.append(
                EmbeddingRecord(
                    chunk_id=chunk.chunk_id,
                    embedding=embedding.tolist(),
                    model_name=self.model_name,
                    embedding_dimension=len(embedding),
                    metadata=chunk.metadata.copy(),
                )
            )
        return records