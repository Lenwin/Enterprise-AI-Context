from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post(
    "/upload",
    response_model=DocumentResponse,
)
def upload_document(
    file: UploadFile = File(...),
    uploaded_by: int = Form(...),
    db: Session = Depends(get_db),
):
    return DocumentService.create_document(
        db=db,
        file=file,
        uploaded_by=uploaded_by,
    )


@router.get(
    "/",
    response_model=list[DocumentResponse],
)
def get_documents(
    search: str | None = None,
    source: str | None = None,
    page: int = 1,
    limit: int = 10,
    sort: str = "desc",
    db: Session = Depends(get_db),
):
    return DocumentService.get_all_documents(
        db=db,
        search=search,
        source=source,
        page=page,
        limit=limit,
        sort=sort,
    )

@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
)
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):

    document = DocumentService.get_document(
        db=db,
        document_id=document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return document


@router.get("/{document_id}/download")
def download_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = DocumentService.get_document_file(
        db=db,
        document_id=document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return FileResponse(
        path=document.file_path,
        filename=document.original_filename,
        media_type=document.mime_type,
    )


@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
):

    document = DocumentService.delete_document(
        db=db,
        document_id=document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return {
        "message": "Document deactivated successfully."
    }