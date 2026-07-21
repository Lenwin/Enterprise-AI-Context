from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.models.chunk import DocumentChunk
from src.models.document import EnterpriseDocument

class RecursiveDocumentChunker:
    def __init__(self,chunk_size:int = 500,chunk_overlap:int = 100,):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ],
        )
    def chunk_document(self,document:EnterpriseDocument)->list[DocumentChunk]:
        chunks = self.splitter.split_text(document.content)
        document_chunks: list[DocumentChunk] = []
        for index,chunk in enumerate(chunks):
            document_chunks.append(
                DocumentChunk(chunk_id=f"{document.id}_chunk_{index}",
                              document_id = document.id,
                              chunk_index = index,
                              content = chunk,
                              source = document.source,
                              metadata = document.metadata.copy()
                              )
            )
        return document_chunks
    
    def chunk_documents(self,documents: list[EnterpriseDocument])->list[DocumentChunk]:
        all_chunks:list[DocumentChunk] = []
        for document in documents:
            all_chunks.extend(
                self.chunk_document(document)
            )
        return all_chunks
