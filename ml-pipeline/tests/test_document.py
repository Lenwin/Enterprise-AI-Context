from src.models.document import EnterpriseDocument

doc = EnterpriseDocument(
    id="123",
    title="Leave Policy",
    content="Employees receive 20 annual leave days.",
    source="SharePoint",
)

print(doc.model_dump())