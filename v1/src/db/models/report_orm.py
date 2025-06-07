"""reports - Отчёты по всем видам данных: ТО, заправки, эффективность, финансовые метрики. Сохраняются в JSON, можно повторно открывать."""
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, JSON, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class ReportOrm(BaseOrm):
    __tablename__ = "reports"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    type: Mapped[str] = mapped_column(String, index=True)
    created_by: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    generated_at: Mapped[datetime] = mapped_column(DateTime, index=True)
    payload: Mapped[dict] = mapped_column(JSON)

    __table_args__ = (
        # Уникальный отчёт по типу, автору и дате генерации (например, ежедневный отчет пользователя по типу)
        UniqueConstraint("type", "created_by", "generated_at", name="uq_report_type_author_date"),
        # Индекс для поиска всех отчетов конкретного пользователя по типу за период
        Index("ix_report_type_author_date", "type", "created_by", "generated_at"),
    )
