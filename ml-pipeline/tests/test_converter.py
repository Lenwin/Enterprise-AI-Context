from src.ingestion.loader import EnterpriseDatasetLoader
from src.ingestion.converter import EnterpriseDocumentConverter

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
loader = EnterpriseDatasetLoader()
dataset = loader.load_from_disk(PROJECT_ROOT /"data"/"demo-enterprise"/"data"/"demo-enterprise"/"enterprise-rag-1000")

raw_record = dataset[0]

document = EnterpriseDocumentConverter.convert(raw_record)

print(document)
print()
print(document.model_dump())

