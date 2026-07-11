from src.ingestion.loader import EnterpriseDatasetLoader
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
loader = EnterpriseDatasetLoader()
dataset = loader.load_from_disk(PROJECT_ROOT /"data"/"demo-enterprise"/"data"/"demo-enterprise"/"enterprise-rag-1000")

print("Documents:", loader.num_documents())

print()

print("Features:")

print(loader.features())

print()

# print("Sources:")

#print(loader.source_types())

#print()

print(loader.sample())