from src.indexing.indexer import EnterpriseIndexer
from src.models.document import EnterpriseDocument
from src.retrieval.query import RetrievalQuery
from src.retrieval.retriever import EnterpriseRetriever
from src.vectorstore.qdrant_store import EnterpriseQdrantStore


def main():

    store = EnterpriseQdrantStore(
        embedding_dimension=768,
        in_memory=True,
    )

    store.create_collection()

    document = EnterpriseDocument(
        id="doc_001",
        title="Leave Policy",
        content="""
Employees receive 20 annual leave days every year.

Medical leave requires supporting documents.

Unused leave can be carried forward.
""",
        source="Confluence",
        metadata={
            "department": "HR"
        }
    )

    indexer = EnterpriseIndexer(store)
    indexer.index_documents([document])

    retriever = EnterpriseRetriever(store)

    results = retriever.retrieve(
        RetrievalQuery(
            query="annual leave",
            top_k=3,
        )
    )

    print(f"Retrieved: {len(results)}")

    print("-" * 50)

    for result in results:
        print(result)
        print("-" * 50)


if __name__ == "__main__":
    main()