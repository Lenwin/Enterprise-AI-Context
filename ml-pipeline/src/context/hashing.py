import hashlib

from src.models.document import EnterpriseDocument

class DocumentHasher:
    @staticmethod
    def hash_document(document: EnterpriseDocument)->str:

        text = (document.title+document.content+document.source)
        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()