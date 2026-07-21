from src.vectorstore.qdrant_store import EnterpriseQdrantStore

def main():

    store = EnterpriseQdrantStore(in_memory = True)
    print("Collections Exists")
    print(store.collection_exists())

    print()

    print("Point Count:")
    print(store.count())
if __name__=="__main__":
    main()