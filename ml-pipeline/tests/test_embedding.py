from src.embeddings.embedder import EnterpriseEmbedder
from src.models.chunk import DocumentChunk


def main():

    chunk = DocumentChunk(
        chunk_id="chunk_001",
        document_id="doc_001",
        chunk_index=0,
        content="Employees receive twenty annual leave days.",
        source="Confluence",
        metadata={"department": "HR"},
    )

    embedder = EnterpriseEmbedder()

    record = embedder.embed_chunk(chunk)

    print(f"Chunk ID      : {record.chunk_id}")
    print(f"Model         : {record.model_name}")
    print(f"Dimension     : {record.embedding_dimension}")
    print(f"Metadata      : {record.metadata}")

    print()
    print(f"First 10 Values:\n{record.embedding[:10]}")


if __name__ == "__main__":
    main()