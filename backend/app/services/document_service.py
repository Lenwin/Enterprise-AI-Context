from sqlalchemy.orm import Session

from app.clients.ml_client import MLClient
from app.db.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentCreate


class DocumentService:

    @staticmethod
    def create_document(
        db: Session,
        document_data: DocumentCreate,
    ) -> Document:

        document = Document(
            filename=document_data.filename,
            source=document_data.source.value,
            status="uploaded",
            version=1,
            uploaded_by=document_data.uploaded_by,
            is_active=True,
        )

        document = DocumentRepository.create(
            db=db,
            document=document,
        )

        MLClient.ingest_document(document.id)

        return document

    @staticmethod
    def get_all_documents(
        db: Session,
    ):
        return DocumentRepository.get_all(db)

    @staticmethod
    def get_document(
        db: Session,
        document_id: int,
    ):
        return DocumentRepository.get_by_id(
            db=db,
            document_id=document_id,
        )

    @staticmethod
    def delete_document(
        db: Session,
        document_id: int,
    ):
        document = DocumentRepository.get_by_id(
            db=db,
            document_id=document_id,
        )

        if document is None:
            return None

        return DocumentRepository.soft_delete(
            db=db,
            document=document,
        )