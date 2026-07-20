from enum import Enum


class DocumentSource(str, Enum):
    PDF = "pdf"
    GITHUB = "github"
    JIRA = "jira"
    SLACK = "slack"
    CONFLUENCE = "confluence"
    DATABASE = "database"


class DocumentStatus(str, Enum):
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    INDEXED = "indexed"
    FAILED = "failed"


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"