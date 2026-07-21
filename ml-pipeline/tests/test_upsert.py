from src.vectorstore.qdrant_store import EnterpriseQdrantStore
from src.models.embedding import EmbeddingRecord

def main():
    store = EnterpriseQdrantStore(embedding_dimension=768,in_memory=True)
    store.create_collection()
    records = [
        EmbeddingRecord(
            chunk_id="chunk_001",
            embedding = [0.1]*768,
            model_name = "BAAI/bge-base-en-v1.5",
            embedding_dimension = 768,
            metadata={
                "department": "HR",
                "source": "Confluence"
            },
        ),
        EmbeddingRecord(
            chunk_id="chunk_002",
            embedding = [0.2]*768,
            model_name = "BAAI/bge-base-en-v1.5",
            embedding_dimension = 768,
            metadata={
                "department": "Engineering",
                "source": "Github"
            }
        )
    ]
    store.upsert(records)

    print("Points in collection:",store.count())

if __name__ == "__main__":
    main()
