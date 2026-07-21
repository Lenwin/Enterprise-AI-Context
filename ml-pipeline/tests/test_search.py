from src.embeddings.embedder import EnterpriseEmbedder
from src.models.chunk import DocumentChunk
from src.vectorstore.qdrant_store import EnterpriseQdrantStore

def main():

    embedder = EnterpriseEmbedder()

    chunk = DocumentChunk(
        chunk_id = "chunk_001",
        document_id = "doc_001",
        chunk_index = 0,
        content = "Employees recieve 20 annual leave days every calendar year",
        source = "Confluence",
        metadata = {
            "department":"HR"
        }
    )
    record = embedder.embed_chunk(chunk)

    store = EnterpriseQdrantStore(
        embedding_dimension=record.embedding_dimension,
        in_memory=True
    )

    store.create_collection()
    store.upsert([record])
    query = embedder.embed_query(
        "How many leave days do employees get?"
    )
    results = store.search(query)

    print(f"Results Found: {len(results)}")
    print("-"*50)

    for result in results:
        print(result)
if __name__ == "__main__":
    main()