"""ml_suggestions - ИИ-подсказки: прогнозы поломок, маршруты, предложения по оптимизации. Хранит текстовое описание, статус (решено/нет), ссылку на объект."""
from datetime import datetime

from sqlalchemy import String, Text, Boolean, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class MlSuggestionOrm(BaseOrm):
    __tablename__ = "ml_suggestions"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    suggestion_type: Mapped[str] = mapped_column(String, index=True)
    target_entity: Mapped[str] = mapped_column(String, index=True)
    entity_id: Mapped[str] = mapped_column(String, index=True)
    message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, index=True)
    resolved: Mapped[bool] = mapped_column(Boolean, index=True)

    __table_args__ = (
        Index("ix_ml_suggestions_target_entity_id", "target_entity", "entity_id"),
        Index("ix_ml_suggestions_unresolved_type", "suggestion_type", "resolved"),
        UniqueConstraint(
            "suggestion_type", "target_entity", "entity_id", "resolved",
            name="uq_ml_suggestion_active"
        ),
    )
