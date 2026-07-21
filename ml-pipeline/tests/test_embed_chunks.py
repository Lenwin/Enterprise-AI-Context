from src.embeddings.embedder import EnterpriseEmbedder
from src.models.chunk import DocumentChunk


def main():

    chunks = [
        DocumentChunk(
            chunk_id="chunk_001",
            document_id="doc_001",
            chunk_index=0,
            content="Employees receive twenty annual leave days.",
            source="Confluence",
            metadata={"department": "HR"},
        ),

        DocumentChunk(
            chunk_id="chunk_002",
            document_id="doc_001",
            chunk_index=1,
            content="Medical leave requires supporting documents.",
            source="Confluence",
            metadata={"department": "HR"},
        ),

        DocumentChunk(
            chunk_id="chunk_003",
            document_id="doc_002",
            chunk_index=0,
            content="Performance reviews are conducted twice every year.",
            source="Confluence",
            metadata={"department": "Management"},
        ),
    ]

    embedder = EnterpriseEmbedder()

    records = embedder.embed_chunks(chunks)

    print(f"Total Embeddings : {len(records)}")
    print("-" * 60)

    for record in records:

        print(f"Chunk ID      : {record.chunk_id}")
        print(f"Model         : {record.model_name}")
        print(f"Dimension     : {record.embedding_dimension}")
        print(f"Metadata      : {record.metadata}")

        print("First 5 Values:")
        print(record.embedding[:5])

        print("-" * 60)

if __name__ == "__main__":
    main()