"""ml_suggestions - ИИ-подсказки: прогнозы поломок, маршруты, предложения по оптимизации. Хранит текстовое описание, статус (решено/нет), ссылку на объект."""
from datetime import datetime

from sqlalchemy import String, Text, Boolean, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class MlSuggestionOrm(BaseOrm):
    __tablename__ = "ml_suggestions"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    suggestion_type: Mapped[str] = mapped_column(String)
    target_entity: Mapped[str] = mapped_column(String)
    entity_id: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    resolved: Mapped[bool] = mapped_column(Boolean)
