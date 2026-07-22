import json 
from pathlib import Path
from datetime import datetime

from src.models.document_manifest import DocumentManifest

class ManifestManager:
    def __init__(self,manifest_path:str|Path = "manifest.json"):
        self.manifest_path = Path(manifest_path)

        if not self.manifest_path.exists():
            self.manifest_path.write_text("{}")

    def load(self)->dict[str,DocumentManifest]:

        data = json.loads(self.manifest_path.read_text())
        return{
            document_id:DocumentManifest(**entry)
            for document_id,entry in data.items()
        }
    def save(self,manifest:dict[str,DocumentManifest]):
        data = {
            document_id:entry.model_dump(mode="json")
            for document_id,entry in manifest.items()
        }
        self.manifest_path.write_text(
            json.dumps(data,indent=4)
        )
    def update(
            self,
            document_id:str,
            document_hash:str
    ):
        manifest = self.load()
        manifest[document_id] = DocumentManifest(
            document_id=document_id,
            document_hash=document_hash,
            indexed_at = datetime.utcnow(),
        )
        self.save(manifest)
    def remove(
        self,
        document_id: str,
    ) -> None:

        manifest = self.load()

        if document_id in manifest:
            del manifest[document_id]

        self.save(manifest)