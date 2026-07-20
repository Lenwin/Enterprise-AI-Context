class MLClient:

    @staticmethod
    def ingest_document(document_id: int) -> dict:

        return {
            "status": "queued",
            "document_id": document_id,
            "message": "Document queued for ML processing."
        }