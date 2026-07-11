from pydantic import ValidationError
from src.models.document import EnterpriseDocument

class EnterpriseDocumentValidator:

    MIN_CONTENT_LENGTH = 20
    @classmethod
    def validate(cls,document:EnterpriseDocument)->tuple[bool,list[str]]:
        errors = []

        if not document.id.strip():
            errors.append("Document ID is empty.")
        if not document.title.strip():
            errors.append("Document title is empty.")
        if not document.content.strip():
            errors.append("Document content is empty.")
        if not document.source.strip():
            errors.append("Document source is empty.")
        
        if len(document.content.strip())<cls.MIN_CONTENT_LENGTH:
            errors.append(f"Content is shorter than {cls.MIN_CONTENT_LENGTH} characters.")
        
        return len(errors)==0,errors