from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.core.enums import DocumentSource


class DocumentCreate(BaseModel):
    filename: str
    source: DocumentSource
    uploaded_by: int


class DocumentResponse(BaseModel):
    id: int
    filename: str
    source: str
    status: str
    version: int
    uploaded_by: int
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)