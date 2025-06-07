"""repair_requests - Заявки на ремонт: описание проблемы, статус, приоритет, кто подал и кто одобрил. Используется диспетчерами и механиками для планирования и выполнения работ."""
from datetime import datetime

from sqlalchemy import String, Text, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class RepairRequestOrm(BaseOrm):
    __tablename__ = "repair_requests"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"))
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String)
    priority: Mapped[str] = mapped_column(String)
    requested_by: Mapped[str] = mapped_column(ForeignKey("users.id"))
    approved_by: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    closed_at: Mapped[datetime] = mapped_column(DateTime)
