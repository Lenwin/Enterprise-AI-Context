from src.models.chunk import DocumentChunk
def test_chunk():
    chunk = DocumentChunk(
        chunk_id="doc_001_chunk_0",
        document_id="doc_001",
        chunk_index=0,
        content="""
        Employees are entitled to 20 annual leave days.
        Leave requests must be approved by the manager.
        """,
        source="Confluence",
    )

    print("Chunk Created Successfully")
    print("-" * 50)

    print(f"Chunk ID       : {chunk.chunk_id}")
    print(f"Document ID    : {chunk.document_id}")
    print(f"Chunk Index    : {chunk.chunk_index}")
    print(f"Source         : {chunk.source}")
    print(f"Word Count     : {chunk.word_count}")
    print(f"Character Count: {chunk.character_count}")

    print("\nContent:")
    print(chunk.content)

    print("\nMetadata:")
    print(chunk.metadata)

def main():
    test_chunk()

if __name__ == "__main__":
    main()
    