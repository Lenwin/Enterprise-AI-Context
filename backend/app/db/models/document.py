from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models.base_model import BaseModel


class Document(BaseModel):
    __tablename__ = "documents"

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    source: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="uploaded",
        nullable=False,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    uploaded_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )