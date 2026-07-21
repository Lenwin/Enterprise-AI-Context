from src.ingestion.pipeline import EnterpriseIngestionPipeline
from pathlib import Path

def main():
    pipeline = EnterpriseIngestionPipeline()

    chunks,errors = pipeline.run(Path("../data")/"demo-enterprise"/"data"/"demo-enterprise"/"enterprise-rag-1000")
    print(f"Valid Documents : {len(chunks)}")
    print(f"Invalid Documents : {len(errors)}")

    print()

    print(chunks[0])

if __name__ == "__main__":
    main()