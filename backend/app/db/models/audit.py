from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models.base_model import BaseModel


class Audit(BaseModel):
    __tablename__ = "audit_logs"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )

    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    resource: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    details: Mapped[str] = mapped_column(
        Text,
        default="",
    )