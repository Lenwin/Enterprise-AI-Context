from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Embeddings
    embedding_model: str = "BAAI/bge-base-en-v1.5"

    # Reranker
    reranker_model: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    # Ollama
    ollama_model: str = "qwen3:4b"

    # Chunking
    chunk_size: int = 500
    chunk_overlap: int = 100

    # Vector Store
    collection_name: str = "enterprise_documents"

    embedding_dimension: int = 768

    class Config:
        env_file = ".env"


settings = Settings()