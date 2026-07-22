from src.context.hashing import DocumentHasher
from src.models.document import EnterpriseDocument

def main():

    document = EnterpriseDocument(
        id = "doc_001",
        title = "Leave Policy",
        content = "Employees receive 20 annual leave days.",
        source="Confluence"
    )

    fingerprint = DocumentHasher.hash_document(document)

    print("Fingerprint")
    print(fingerprint)

if __name__=="__main__":
    main()