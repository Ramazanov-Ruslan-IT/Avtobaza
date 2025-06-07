"""financial_transactions - Финансовые записи: вид операции (топливо, ремонт и др.), сумма, валюта, дата, связанный автомобиль и пользователь. Позволяет вести бюджет и формировать отчёты."""
from datetime import datetime

from sqlalchemy import String, Text, DateTime, ForeignKey, Numeric, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class FinancialTransactionOrm(BaseOrm):
    __tablename__ = "financial_transactions"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    transaction_type: Mapped[str] = mapped_column(String, index=True)
    category: Mapped[str] = mapped_column(String, index=True)
    amount: Mapped[float] = mapped_column(Numeric)
    currency: Mapped[str] = mapped_column(String, index=True)
    date: Mapped[datetime] = mapped_column(DateTime, index=True)
    vehicle_id: Mapped[str] = mapped_column(String, index=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    description: Mapped[str] = mapped_column(Text)

    __table_args__ = (
        # Композитный индекс для быстрых аналитических выборок
        Index("ix_fintrans_date_vehicle", "date", "vehicle_id"),
        Index("ix_fintrans_type_user", "transaction_type", "user_id"),
        # Уникальность для предотвращения дублей (например, для загружаемых извне операций)
        UniqueConstraint("transaction_type", "amount", "currency", "date", "vehicle_id", "user_id", name="uq_fintrans_main"),
    )
