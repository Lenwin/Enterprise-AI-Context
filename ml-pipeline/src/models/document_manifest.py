from datetime import datetime
from pydantic import BaseModel

class DocumentManifest(BaseModel):

    document_id:str
    document_hash:str
    indexed_at:datetime