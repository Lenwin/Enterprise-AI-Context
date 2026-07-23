from src.chunking.chunker import RecursiveDocumentChunker
from src.indexing.indexer import EnterpriseIndexer
from src.models.document import EnterpriseDocument
from src.retrieval.bm25 import BM25Retriever
from src.retrieval.hybrid import HybridRetriever
from src.retrieval.query import RetrievalQuery
from src.retrieval.retriever import EnterpriseRetriever
from src.vectorstore.qdrant_store import EnterpriseQdrantStore


def main():

    documents = [

        EnterpriseDocument(
            id="doc_hr",
            title="Leave Policy",
            content="""
Employees receive 20 annual leave days every calendar year.

Medical leave requires supporting documents.

Unused leave can be carried forward.
""",
            source="Confluence",
            metadata={
                "department": "HR"
            }
        ),

        EnterpriseDocument(
            id="doc_platform",
            title="Kubernetes Guide",
            content="""
Deploy applications using Kubernetes.

Pods are automatically restarted after failure.

Rolling deployments minimize downtime.
""",
            source="GitHub",
            metadata={
                "department": "Platform"
            }
        ),

        EnterpriseDocument(
            id="doc_finance",
            title="Expense Policy",
            content="""
Employees can claim travel expenses.

Manager approval is required before reimbursement.
""",
            source="Confluence",
            metadata={
                "department": "Finance"
            }
        ),
    ]

    # -----------------------------
    # Vector Store
    # -----------------------------
    store = EnterpriseQdrantStore(
        embedding_dimension=768,
        in_memory=True,
    )

    store.create_collection()

    indexer = EnterpriseIndexer(store)
    indexer.index_documents(documents)

    # -----------------------------
    # BM25 Index
    # -----------------------------
    chunker = RecursiveDocumentChunker()

    chunks = chunker.chunk_documents(documents)

    bm25 = BM25Retriever()
    bm25.index(chunks)

    # -----------------------------
    # Hybrid Retriever
    # -----------------------------
    vector = EnterpriseRetriever(store)

    hybrid = HybridRetriever(
        vector_retriever=vector,
        bm25_retriever=bm25,
    )

    # -----------------------------
    # Search
    # -----------------------------
    results = hybrid.retrieve(
        RetrievalQuery(
            query="annual leave policy",
            top_k=5,
        )
    )

    print(f"Results Found: {len(results)}")
    print("-" * 60)

    for i, result in enumerate(results, start=1):
        print(f"Rank : {i}")
        print(f"Chunk ID : {result.chunk_id}")
        print(f"Document : {result.document_id}")
        print(f"Score : {result.score:.4f}")
        print(f"Source : {result.source}")
        print(f"Metadata : {result.metadata}")
        print(result.content)
        print("-" * 60)


if __name__ == "__main__":
    main()