from sqlalchemy.orm import Session

from app.db.models.document import Document


class DocumentRepository:

    @staticmethod
    def create(
        db: Session,
        document: Document,
    ) -> Document:

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def get_all(
        db: Session,
    ) -> list[Document]:

        return db.query(Document).all()

    @staticmethod
    def get_by_id(
        db: Session,
        document_id: int,
    ) -> Document | None:

        return (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    @staticmethod
    def soft_delete(
        db: Session,
        document: Document,
    ) -> Document:

        document.is_active = False

        db.commit()
        db.refresh(document)

        return document