from src.indexing.indexer import EnterpriseIndexer
from src.llm.ollama_client import OllamaClient
from src.llm.rag_pipeline import EnterpriseRAGPipeline
from src.models.document import EnterpriseDocument
from src.retrieval.bm25 import BM25Retriever
from src.retrieval.hybrid import HybridRetriever
from src.retrieval.reranker import CrossEncoderReranker
from src.retrieval.retriever import EnterpriseRetriever
from src.vectorstore.qdrant_store import EnterpriseQdrantStore
from src.chunking.chunker import RecursiveDocumentChunker


def main():

    # ----------------------------
    # Sample Enterprise Documents
    # ----------------------------
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
            metadata={"department": "HR"},
        ),

        EnterpriseDocument(
            id="doc_it",
            title="Kubernetes Guide",
            content="""
Applications are deployed using Kubernetes.

Pods automatically restart after failure.

Rolling updates minimize downtime.
""",
            source="GitHub",
            metadata={"department": "Platform"},
        ),

        EnterpriseDocument(
            id="doc_finance",
            title="Expense Policy",
            content="""
Travel expenses require manager approval.

Receipts must be submitted within 30 days.
""",
            source="Confluence",
            metadata={"department": "Finance"},
        ),
    ]

    # ----------------------------
    # Vector Store
    # ----------------------------
    store = EnterpriseQdrantStore(
        embedding_dimension=768,
        in_memory=True,
    )

    store.create_collection()

    # ----------------------------
    # Index Documents
    # ----------------------------
    indexer = EnterpriseIndexer(store)
    indexer.index_documents(documents)

    # ----------------------------
    # BM25 Index
    # ----------------------------
    chunker = RecursiveDocumentChunker()

    chunks = chunker.chunk_documents(documents)

    bm25 = BM25Retriever()
    bm25.index(chunks)

    # ----------------------------
    # Retriever
    # ----------------------------
    vector = EnterpriseRetriever(store)

    hybrid = HybridRetriever(
        vector_retriever=vector,
        bm25_retriever=bm25,
    )

    # ----------------------------
    # Reranker
    # ----------------------------
    reranker = CrossEncoderReranker()

    # ----------------------------
    # LLM
    # ----------------------------
    llm = OllamaClient(
        model_name="qwen3:4b",   # Change if you're using another model
    )

    # ----------------------------
    # RAG Pipeline
    # ----------------------------
    rag = EnterpriseRAGPipeline(
        retriever=hybrid,
        reranker=reranker,
        llm=llm,
    )

    # ----------------------------
    # Ask Question
    # ----------------------------
    response = rag.ask(
        "How many annual leave days do employees receive?"
    )

    print("=" * 80)
    print("ANSWER")
    print("=" * 80)
    print(response.answer)
    print()

    print("=" * 80)
    print("MODEL")
    print("=" * 80)
    print(response.model_name)

    print()

    print("=" * 80)
    print("TOKENS")
    print("=" * 80)
    print("Prompt:", response.prompt_tokens)
    print("Completion:", response.completion_tokens)
    print("Total:", response.total_tokens)

    print()

    print("=" * 80)
    print("LATENCY")
    print("=" * 80)
    print(f"{response.latency_ms:.2f} ms")


if __name__ == "__main__":
    main()