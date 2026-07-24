from src.retrieval.context_builder import ContextBuilder
from src.models.search_result import SearchResult


def main():

    results = [

        SearchResult(
            chunk_id="chunk_1",
            document_id="doc_1",
            chunk_index=0,
            score=0.95,
            source="Confluence",
            content="Employees receive 20 annual leave days.",
            metadata={"department": "HR"},
        ),

        SearchResult(
            chunk_id="chunk_2",
            document_id="doc_2",
            chunk_index=0,
            score=0.82,
            source="GitHub",
            content="Pods restart automatically after failure.",
            metadata={"department": "Platform"},
        ),
    ]

    builder = ContextBuilder()

    context = builder.build(results)

    print(context)


if __name__ == "__main__":
    main()