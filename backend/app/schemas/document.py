from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DocumentResponse(BaseModel):
    id: int
    original_filename: str
    stored_filename: str
    file_path: str
    file_size: int
    mime_type: str
    source: str
    status: str
    version: int
    uploaded_by: int
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)