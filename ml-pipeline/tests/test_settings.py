from src.config.settings import settings


def main():

    print("Embedding Model :", settings.embedding_model)
    print("Reranker Model  :", settings.reranker_model)
    print("Ollama Model    :", settings.ollama_model)
    print("Chunk Size      :", settings.chunk_size)
    print("Chunk Overlap   :", settings.chunk_overlap)
    print("Collection Name :", settings.collection_name)
    print("Embedding Dim   :", settings.embedding_dimension)


if __name__ == "__main__":
    main()