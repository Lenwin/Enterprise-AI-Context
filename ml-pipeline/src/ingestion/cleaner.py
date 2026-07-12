import re
from src.models.document import EnterpriseDocument

class EnterpriseDocumentCleaner:

    @staticmethod
    def clean(document:EnterpriseDocument)->EnterpriseDocument:
        document.title = EnterpriseDocumentCleaner._clean_text(document.title)
        document.content = EnterpriseDocumentCleaner._clean_text(document.content)

        return document
    
    @staticmethod
    def clean_all(documents:list[EnterpriseDocument],)->list[EnterpriseDocument]:
        return [EnterpriseDocumentCleaner.clean(document) for document in documents]

    @staticmethod

    def _clean_text(text:str)->str:
        if not text:
            return ""
        
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        text = text.replace("\t", " ")

        text = "\n".join(line.rstrip() for line in text.split("\n"))

        text = re.sub(r"[ ]{2,}", " ", text)

        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()
