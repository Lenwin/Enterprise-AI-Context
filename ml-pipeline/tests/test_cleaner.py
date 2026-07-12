from src.models.document import EnterpriseDocument
from src.ingestion.cleaner import EnterpriseDocumentCleaner

def test_clean_document():
    document = EnterpriseDocument(
        id="1",
        title="   Sample\tTitle   ",
        content="Hello\t\tWorld\n\n\n\nThis    is    a   test.\r\n",
        source="pdf",
    )
    cleaned = EnterpriseDocumentCleaner.clean(document)

    print(cleaned.title)
    print(cleaned.content)

if __name__ =="__main__":
    test_clean_document()