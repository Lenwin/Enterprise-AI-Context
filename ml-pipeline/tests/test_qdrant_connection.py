from qdrant_client import QdrantClient

def main():
    client = QdrantClient(":memory:")
    print("Connected Successfully")
    collections = client.get_collections()
    print(collections)

if __name__=="__main__":
    main()