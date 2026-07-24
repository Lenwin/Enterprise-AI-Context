from src.chunking.chunker import RecursiveDocumentChunker
from src.indexing.indexer import EnterpriseIndexer
from src.models.document import EnterpriseDocument
from src.retrieval.bm25 import BM25Retriever
from src.retrieval.hybrid import HybridRetriever
from src.retrieval.query import RetrievalQuery
from src.retrieval.reranker import CrossEncoderReranker
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

Unused leave can be carried forward up to 10 days.
""",
            source="Confluence",
            metadata={"department": "HR"},
        ),

        EnterpriseDocument(
            id="doc_platform",
            title="Kubernetes Guide",
            content="""
Deploy applications using Kubernetes.

Pods automatically restart after failure.

Rolling deployments reduce downtime.
""",
            source="GitHub",
            metadata={"department": "Platform"},
        ),

        EnterpriseDocument(
            id="doc_finance",
            title="Expense Policy",
            content="""
Employees may claim travel expenses.

Manager approval is required before reimbursement.
""",
            source="Confluence",
            metadata={"department": "Finance"},
        ),
    ]

    # -----------------------------
    # Vector Index
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
    # Hybrid Retrieval
    # -----------------------------
    vector = EnterpriseRetriever(store)

    hybrid = HybridRetriever(
        vector_retriever=vector,
        bm25_retriever=bm25,
    )

    results = hybrid.retrieve(
        RetrievalQuery(
            query="How many annual leave days do employees receive?",
            top_k=10,
        )
    )

    print("\nHybrid Results")
    print("=" * 70)

    for r in results:
        print(f"{r.score:.4f} | {r.document_id}")
        print(r.content)
        print("-" * 70)

    # -----------------------------
    # Reranking
    # -----------------------------
    reranker = CrossEncoderReranker()

    reranked = reranker.rerank(
        query="How many annual leave days do employees receive?",
        results=results,
        top_k=5,
    )

    print("\nReranked Results")
    print("=" * 70)

    for i, r in enumerate(reranked, start=1):
        print(f"Rank: {i}")
        print(f"Score: {r.score:.4f}")
        print(f"Document: {r.document_id}")
        print(f"Chunk: {r.chunk_id}")
        print(f"Source: {r.source}")
        print(r.content)
        print("-" * 70)


if __name__ == "__main__":
    main()