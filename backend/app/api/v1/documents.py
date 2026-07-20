from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.document import DocumentCreate, DocumentResponse
from app.services.document_service import DocumentService

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post(
    "/upload",
    response_model=DocumentResponse,
)
def upload_document(
    document: DocumentCreate,
    db: Session = Depends(get_db),
):
    return DocumentService.create_document(
        db=db,
        document_data=document,
    )


@router.get(
    "/",
    response_model=list[DocumentResponse],
)
def get_documents(
    db: Session = Depends(get_db),
):
    return DocumentService.get_all_documents(db)


@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
)
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):

    document = DocumentService.get_document(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return document


@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
):

    document = DocumentService.delete_document(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return {
        "message": "Document deleted successfully."
    }