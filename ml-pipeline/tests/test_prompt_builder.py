from src.llm.prompt_builder import PromptBuilder
from src.retrieval.query import RetrievalQuery


def main():

    context = """
Document 1

Employees receive 20 annual leave days.

Document 2

Medical leave requires supporting documents.
"""

    query = RetrievalQuery(
        query="How many annual leave days do employees receive?"
    )

    builder = PromptBuilder()

    prompt = builder.build(
        query=query,
        context=context,
    )

    print(prompt)


if __name__ == "__main__":
    main()