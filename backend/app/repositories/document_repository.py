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
        search: str | None = None,
        source: str | None = None,
        page: int = 1,
        limit: int = 10,
        sort: str = "desc",
    ) -> list[Document]:

        query = db.query(Document).filter(Document.is_active == True)

        if search:
            query = query.filter(
                Document.original_filename.ilike(f"%{search}%")
            )

        if source:
            query = query.filter(
                Document.source == source
            )

        if sort.lower() == "asc":
            query = query.order_by(Document.created_at.asc())
        else:
            query = query.order_by(Document.created_at.desc())

        offset = (page - 1) * limit

        return (
            query
            .offset(offset)
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        document_id: int,
    ) -> Document | None:

        return (
            db.query(Document)
            .filter(
                Document.id == document_id,
                Document.is_active == True,
            )
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