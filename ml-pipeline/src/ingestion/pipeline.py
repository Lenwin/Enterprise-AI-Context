from pathlib import Path

from src.ingestion.cleaner import EnterpriseDocumentCleaner
from src.ingestion.converter import EnterpriseDocumentConverter
from src.ingestion.loader import EnterpriseDatasetLoader
from src.ingestion.validator import EnterpriseDocumentValidator
from src.models.document import EnterpriseDocument
from src.chunking.chunker import RecursiveDocumentChunker
from src.models.chunk import DocumentChunk
class EnterpriseIngestionPipeline:
    def __init__(self):
        self.loader = EnterpriseDatasetLoader()
        self.chunker = RecursiveDocumentChunker()
    def run(self,dataset_path:str|Path,)->tuple[list[DocumentChunk],list[tuple[str,list[str]]]]:
        dataset = self.loader.load_from_disk(dataset_path)
        documents = EnterpriseDocumentConverter.convert_dataset(dataset)

        valid_documents:list[EnterpriseDocument] = []
        validation_errors:list[tuple[str,list[str]]]=[]

        for document in documents:

            is_valid,errors = EnterpriseDocumentValidator.validate(document)

            if not is_valid:
                validation_errors.append((document.id,errors))
                continue
            cleaned_document = EnterpriseDocumentCleaner.clean(document)
            valid_documents.append(cleaned_document)

        chunks = self.chunker.chunk_documents(valid_documents)

        return chunks,validation_errors