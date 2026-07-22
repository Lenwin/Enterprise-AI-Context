from src.vectorstore.qdrant_store import EnterpriseQdrantStore
from src.models.chunk import DocumentChunk
from src.embeddings.embedder import EnterpriseEmbedder

def main():

    embedder = EnterpriseEmbedder()
    chunks = [
        DocumentChunk(
            chunk_id="chunk_001",
            document_id="doc_001",
            chunk_index=0,
            content="Employees receive 20 annual leave days.",
            source="Confluence",
        ),
        DocumentChunk(
            chunk_id="chunk_002",
            document_id="doc_001",
            chunk_index=1,
            content="Unused leave may be carried forward.",
            source="Confluence",
        )
    ]

    records = [
        embedder.embed_chunk(chunk)
        for chunk in chunks
    ]

    store = EnterpriseQdrantStore(
        embedding_dimension=records[0].embedding_dimension,
        in_memory=True,
    )

    store.create_collection()

    store.upsert(records)

    print("Before Delete:", store.count())

    store.delete_document("doc_001")

    print("After Delete:", store.count())

if __name__=="__main__":

    main()


