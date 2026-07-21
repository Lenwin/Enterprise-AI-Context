from src.vectorstore.qdrant_store import EnterpriseQdrantStore


def main():

    store = EnterpriseQdrantStore(
        embedding_dimension=768,
        in_memory=True,
    )

    print("Exists Before:")
    print(store.collection_exists())

    store.create_collection()

    print()

    print("Exists After:")
    print(store.collection_exists())

    print()

    print("Point Count:")
    print(store.count())


if __name__ == "__main__":
    main()