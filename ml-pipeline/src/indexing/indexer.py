from src.chunking.chunker import RecursiveDocumentChunker
from src.embeddings.embedder import EnterpriseEmbedder
from src.models.document import EnterpriseDocument
from src.vectorstore.qdrant_store import EnterpriseQdrantStore

class EnterpriseIndexer:

    def __init__(self,store:EnterpriseQdrantStore):
        self.chunker = RecursiveDocumentChunker()
        self.embedder = EnterpriseEmbedder()
        self.store = store

    def index_documents(self,documents:list[EnterpriseDocument]):
        chunks = self.chunker.chunk_documents(documents)
        records = self.embedder.embed_chunks(chunks)
        self.store.upsert(records)
