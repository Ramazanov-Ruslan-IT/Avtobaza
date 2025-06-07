"""reports - Отчёты по всем видам данных: ТО, заправки, эффективность, финансовые метрики. Сохраняются в JSON, можно повторно открывать."""
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, JSON, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class ReportOrm(BaseOrm):
    __tablename__ = "reports"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    type: Mapped[str] = mapped_column(String)
    created_by: Mapped[str] = mapped_column(ForeignKey("users.id"))
    generated_at: Mapped[datetime] = mapped_column(DateTime)
    payload: Mapped[dict] = mapped_column(JSON)
