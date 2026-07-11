from src.ingestion.loader import EnterpriseDatasetLoader

loader = EnterpriseDatasetLoader()

dataset = loader.load_from_disk(
    "/home/lenwin/ANACONDACODES/RAG/Enterprise-AI-Context/data/demo-enterprise/data/demo-enterprise/enterprise-rag-1000"
)

print("Documents:", loader.num_documents())

print()

print("Features:")

print(loader.features())

print()

print("Sources:")

print(loader.source_types())

print()

print(loader.sample())