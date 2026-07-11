from typing import Any
from src.models.document import EnterpriseDocument

class EnterpriseDocumentConverter:
    def convert(record:dict[str,Any])->EnterpriseDocument:
        return EnterpriseDocument(
            id = record["doc_id"],
            title = record["title"],
            content = record["content"],
            source = record["source_type"],

            document_type = "unknown",
            department = "unknown",
            metadata = {}
        )
    def convert_dataset(records):
        return [
            EnterpriseDocumentConverter.convert(record)
            for record in records
        ]