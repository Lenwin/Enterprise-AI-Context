from src.ingestion.pipeline import EnterpriseIngestionPipeline
from pathlib import Path

def main():
    pipeline = EnterpriseIngestionPipeline()

    documents,errors = pipeline.run(Path("../data")/"demo-enterprise"/"data"/"demo-enterprise"/"enterprise-rag-1000")
    print(f"Valid Documents : {len(documents)}")
    print(f"Invalid Documents : {len(errors)}")

    print()

    print(documents[0])

if __name__ == "__main__":
    main()