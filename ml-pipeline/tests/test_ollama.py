from src.llm.ollama_client import OllamaClient


def main():

    llm = OllamaClient(
        model_name="qwen3:4b",
    )

    response = llm.generate(
        "Explain what Retrieval-Augmented Generation (RAG) is in three sentences."
    )

    print("Model:", response.model_name)
    print("Latency:", round(response.latency_ms, 2), "ms")
    print()
    print(response.answer)


if __name__ == "__main__":
    main()