from src.chunking.chunker import RecursiveDocumentChunker
from src.indexing.indexer import EnterpriseIndexer
from src.llm.ollama_client import OllamaClient
from src.llm.rag_pipeline import EnterpriseRAGPipeline
from src.models.document import EnterpriseDocument
from src.retrieval.bm25 import BM25Retriever
from src.retrieval.hybrid import HybridRetriever
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

Unused leave can be carried forward up to 10 days.

Medical leave requires supporting documents.
""",
            source="Confluence",
            metadata={
                "department": "HR"
            },
        ),

        EnterpriseDocument(
            id="doc_it",
            title="Kubernetes Guide",
            content="""
Applications are deployed using Kubernetes.

Pods restart automatically after failure.

Rolling updates minimize downtime.
""",
            source="GitHub",
            metadata={
                "department": "Platform"
            },
        ),

        EnterpriseDocument(
            id="doc_finance",
            title="Expense Policy",
            content="""
Travel expenses require manager approval.

Receipts must be submitted within 30 days.
""",
            source="Confluence",
            metadata={
                "department": "Finance"
            },
        ),
    ]

    # -----------------------------
    # Index Documents
    # -----------------------------

    store = EnterpriseQdrantStore(
        embedding_dimension=768,
        in_memory=True,
    )

    store.create_collection()

    indexer = EnterpriseIndexer(store)
    indexer.index_documents(documents)

    # -----------------------------
    # BM25
    # -----------------------------

    chunker = RecursiveDocumentChunker()

    chunks = chunker.chunk_documents(documents)

    bm25 = BM25Retriever()
    bm25.index(chunks)

    # -----------------------------
    # Retrieval
    # -----------------------------

    vector = EnterpriseRetriever(store)

    hybrid = HybridRetriever(
        vector_retriever=vector,
        bm25_retriever=bm25,
    )

    reranker = CrossEncoderReranker()

    llm = OllamaClient()

    rag = EnterpriseRAGPipeline(
        retriever=hybrid,
        reranker=reranker,
        llm=llm,
    )

    # -----------------------------
    # Ask Question
    # -----------------------------

    response = rag.ask(
        "How many annual leave days do employees receive?"
    )

    print("=" * 70)
    print("ANSWER")
    print("=" * 70)

    print(response.answer)

    print()

    print("=" * 70)
    print("SOURCES")
    print("=" * 70)

    for i, source in enumerate(response.sources, start=1):

        print(f"[{i}]")
        print(f"Document ID : {source.document_id}")
        print(f"Chunk ID    : {source.chunk_id}")
        print(f"Source      : {source.source}")
        print(f"Score       : {source.score:.4f}")
        print(f"Content     : {source.content}")
        print("-" * 70)


if __name__ == "__main__":
    main()