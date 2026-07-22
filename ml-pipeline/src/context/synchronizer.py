from src.context.hashing import DocumentHasher
from src.context.manifest import ManifestManager
from src.models.document import EnterpriseDocument

class ContextSynchronizer:
    def __init__(self):
        self.manifest = ManifestManager()
    
    def synchronize(self,documents:list[EnterpriseDocument])->tuple[list[EnterpriseDocument],list[EnterpriseDocument],list[str]]:
        
        current_manifest = self.manifest.load()
        new_documents = []
        updated_documents = []

        current_ids = set()

        for document in documents:
            current_ids.add(document.id)
            document_hash = DocumentHasher.hash_document(document)
            if document.id not in current_manifest:
                new_documents.append(document)
                continue
            if current_manifest[document.id].document_hash!=document_hash:
                updated_documents.append(document)
        
        deleted_documents = []

        for document_id in current_manifest:
            if document_id not in current_ids:

                deleted_documents.append(document_id)
        
        return (
            new_documents,updated_documents,deleted_documents
        )