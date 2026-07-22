from src.context.hashing import DocumentHasher
from src.context.manifest import ManifestManager
from src.context.synchronizer import ContextSynchronizer
from src.models.document import EnterpriseDocument


def main():

    manager = ManifestManager("test_manifest.json")

    document = EnterpriseDocument(
        id="doc_001",
        title="Leave Policy",
        content="Employees receive 20 annual leave days.",
        source="Confluence",
    )

    manager.update(
        document.id,
        DocumentHasher.hash_document(document),
    )

    changed_document = EnterpriseDocument(
        id="doc_001",
        title="Leave Policy",
        content="Employees receive 25 annual leave days.",
        source="Confluence",
    )

    synchronizer = ContextSynchronizer()
    synchronizer.manifest = manager

    new_docs, updated_docs, deleted_docs = synchronizer.synchronize(
        [changed_document]
    )

    print("New Documents:", len(new_docs))
    print("Updated Documents:", len(updated_docs))
    print("Deleted Documents:", len(deleted_docs))

    if updated_docs:
        print(updated_docs[0].content)


if __name__ == "__main__":
    main()