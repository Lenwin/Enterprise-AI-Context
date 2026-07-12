from src.ingestion.validator import EnterpriseDocumentValidator
from src.models.document import EnterpriseDocument

def test_valid_document():
    document = EnterpriseDocument(
        id="123",
        title="Leave Policy",
        content="Employees receive 20 annual leave days every calendar year.",
        source="Confluence",
    )
    is_valid,errors = EnterpriseDocumentValidator.validate(document)

    print("Valid Document")
    print(f"Valid: {is_valid}")
    print(f"Errors: {errors}")
    print("-"*50)

def test_invalid_document():
    document = EnterpriseDocument(
        id = "",
        title = "",
        content = "Short",
        source = ""
    )
    is_valid, errors = EnterpriseDocumentValidator.validate(document)

    print("Invalid Document")
    print(f"Valid: {is_valid}")
    print("Errors:")
    for error in errors:
        print(f" - {error}")
    print("-" * 50)

def main():
    test_valid_document()
    test_invalid_document()

if __name__=="__main__":
    main()
