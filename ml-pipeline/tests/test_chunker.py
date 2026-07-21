from src.chunking.chunker import RecursiveDocumentChunker
from src.models.document import EnterpriseDocument

def main():
    document = EnterpriseDocument(
        id = "doc_001",
        title = "Leave Policy",
        content = """
Employees are entitled to 20 annual leave days.

Leave requests should be submitted through the HR portal.

Unused leave can be carried forward up to 10 days.

Medical leave requires supporting documents.

HR may request additional verification if necessary.

"""*5,
        source = "Confluence",
        metadata = {
            "department":"HR"
        }
    )
    chunker = RecursiveDocumentChunker(
        chunk_size=150,
        chunk_overlap=30
    )
    chunks = chunker.chunk_document(document)
    print(f"Chunks Created: {len(chunks)}")
    print("-"*60)

    for chunk in chunks:
        print(f"Chunk ID     : {chunk.chunk_id}")
        print(f"Document ID  : {chunk.document_id}")
        print(f"Chunk Index  : {chunk.chunk_index}")
        print(f"Word Count   : {chunk.word_count}")
        print(f"Characters   : {chunk.character_count}")
        print(f"Metadata     : {chunk.metadata}")

        print()

        print(chunk.content)

        print("-" * 60)

if __name__ == "__main__":
    main()