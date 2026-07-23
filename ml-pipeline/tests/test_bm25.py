from src.chunking.chunker import RecursiveDocumentChunker
from src.models.document import EnterpriseDocument
from src.retrieval.bm25 import BM25Retriever


def main():

    documents = [

        EnterpriseDocument(
            id="doc_1",
            title="Leave Policy",
            content="""
Employees receive 20 annual leave days.

Medical leave requires approval.
""",
            source="Confluence",
            metadata={
                "department": "HR"
            }
        ),

        EnterpriseDocument(
            id="doc_2",
            title="Kubernetes",
            content="""
Deploy applications using Kubernetes.

Pods can be restarted automatically.
""",
            source="GitHub",
            metadata={
                "department": "Platform"
            }
        ),

        EnterpriseDocument(
            id="doc_3",
            title="Finance",
            content="""
Expense reimbursement policy.

Travel expenses require approval.
""",
            source="Confluence",
            metadata={
                "department": "Finance"
            }
        ),
    ]

    chunker = RecursiveDocumentChunker()

    chunks = chunker.chunk_documents(documents)

    retriever = BM25Retriever()

    retriever.index(chunks)

    results = retriever.search(
        "leave policy",
        top_k=3,
    )

    print(f"Results: {len(results)}")
    print("-" * 60)

    for result in results:
        print(result)
        print("-" * 60)


if __name__ == "__main__":
    main()