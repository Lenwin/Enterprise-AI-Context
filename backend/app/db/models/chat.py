from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models.base_model import BaseModel


class Chat(BaseModel):
    __tablename__ = "chat_history"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )

    question: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    answer: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )