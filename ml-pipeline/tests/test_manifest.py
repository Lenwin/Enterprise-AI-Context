from src.context.manifest import ManifestManager


def main():

    manager = ManifestManager("test_manifest.json")

    manager.update(
        document_id="doc_001",
        document_hash="abc123",
    )

    manager.update(
        document_id="doc_002",
        document_hash="xyz789",
    )

    manifest = manager.load()

    print(f"Documents: {len(manifest)}")
    print("-" * 50)

    for document in manifest.values():
        print(document)


if __name__ == "__main__":
    main()