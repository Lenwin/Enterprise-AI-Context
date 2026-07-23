from src.indexing.indexer import EnterpriseIndexer
from src.models.document import EnterpriseDocument
from src.vectorstore.qdrant_store import EnterpriseQdrantStore

def main():
    document = EnterpriseDocument(
        id="doc_001",
        title = "Leave Policy",
        content = """
Employees receive 20 annual leave days.

Unused leave may be carried forward.

Medical leave requires approval.
""",
        source = "Confluence",
        metadata = {
            "department":"HR"
        }
    )
    store = EnterpriseQdrantStore(
        embedding_dimension=768,
        in_memory=True
    )

    store.create_collection()

    indexer = EnterpriseIndexer(store)

    indexer.index_documents([document])

    print("Points Indexed:",store.count())

if __name__ == "__main__":
    main()