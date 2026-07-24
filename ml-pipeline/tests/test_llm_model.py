from src.llm.response import LLMResponse

def main():

    response = LLMResponse(
        answer="Employees receive 20 annual leave days.",
        model_name="demo-model",
        prompt_tokens=100,
        completion_tokens=20,
        total_tokens=120,
        latency_ms=230,
    )

    print(response)


if __name__ == "__main__":
    main()