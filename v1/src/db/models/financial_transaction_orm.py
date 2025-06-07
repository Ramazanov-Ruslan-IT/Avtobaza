"""financial_transactions - Финансовые записи: вид операции (топливо, ремонт и др.), сумма, валюта, дата, связанный автомобиль и пользователь. Позволяет вести бюджет и формировать отчёты."""
from datetime import datetime

from sqlalchemy import String, Text, DateTime, ForeignKey, Numeric, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class FinancialTransactionOrm(BaseOrm):
    __tablename__ = "financial_transactions"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    transaction_type: Mapped[str] = mapped_column(String)
    category: Mapped[str] = mapped_column(String)
    amount: Mapped[float] = mapped_column(Numeric)
    currency: Mapped[str] = mapped_column(String)
    date: Mapped[datetime] = mapped_column(DateTime)
    vehicle_id: Mapped[str] = mapped_column(String)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    description: Mapped[str] = mapped_column(Text)
