from src.embeddings.embedder import EnterpriseEmbedder
from src.models.chunk import DocumentChunk
from src.vectorstore.qdrant_store import EnterpriseQdrantStore

def main():

    embedder = EnterpriseEmbedder()

    chunks = [

        DocumentChunk(
            chunk_id="chunk_001",
            document_id="doc_hr",
            chunk_index=0,
            content="Employees receive 20 annual leave days.",
            source="Confluence",
            metadata={
                "department": "HR",
            },
        ),

        DocumentChunk(
            chunk_id="chunk_002",
            document_id="doc_eng",
            chunk_index=0,
            content="Deploy microservices using Kubernetes.",
            source="GitHub",
            metadata={
                "department": "Engineering",
            },
        ),
    ]

    records = [
        embedder.embed_chunk(chunk)
        for chunk in chunks
    ]

    store = EnterpriseQdrantStore(embedding_dimension=records[0].embedding_dimension,in_memory=True)

    store.create_collection()
    store.upsert(records)

    query = embedder.embed_query(
        "leave policy"
    )

    results = store.search(
        query_embedding=query,
        filters={
            "department": "HR"
        },
    )

    print("HR Results")
    print("-"*40)

    for result in results:
        print(result)

if __name__=="__main__":
    main()