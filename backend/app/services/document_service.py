from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.clients.ml_client import MLClient
from app.core.file_utils import save_uploaded_file
from app.db.models.document import Document
from app.repositories.document_repository import DocumentRepository


class DocumentService:

    @staticmethod
    def create_document(
        db: Session,
        file: UploadFile,
        uploaded_by: int,
    ) -> Document:

        stored_filename, file_path = save_uploaded_file(file)

        document = Document(
            original_filename=file.filename,
            stored_filename=stored_filename,
            file_path=file_path,
            file_size=file.size if file.size else 0,
            mime_type=file.content_type or "application/octet-stream",
            source=file.filename.split(".")[-1].lower(),
            status="uploaded",
            version=1,
            uploaded_by=uploaded_by,
            is_active=True,
        )

        document = DocumentRepository.create(
            db=db,
            document=document,
        )

        MLClient.ingest_document(
            document_id=document.id,
        )

        return document

    @staticmethod
    def get_all_documents(
        db: Session,
        search: str | None = None,
        source: str | None = None,
        page: int = 1,
        limit: int = 10,
        sort: str = "desc",
    ):

        return DocumentRepository.get_all(
            db=db,
            search=search,
            source=source,
            page=page,
            limit=limit,
            sort=sort,
        )

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
    @staticmethod
    def get_document_file(
        db: Session,
        document_id: int,
    ):

        return DocumentRepository.get_by_id(
            db=db,
            document_id=document_id,
        )