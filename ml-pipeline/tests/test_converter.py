from src.ingestion.loader import EnterpriseDatasetLoader
from src.ingestion.converter import EnterpriseDocumentConverter

loader = EnterpriseDatasetLoader()

dataset = loader.load_from_disk("/home/lenwin/ANACONDACODES/RAG/Enterprise-AI-Context/data/demo-enterprise/data/demo-enterprise/enterprise-rag-1000")

raw_record = dataset[0]

document = EnterpriseDocumentConverter.convert(raw_record)

print(document)
print()
print(document.model_dump())

