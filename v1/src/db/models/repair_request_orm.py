"""repair_requests - Заявки на ремонт: описание проблемы, статус, приоритет, кто подал и кто одобрил. Используется диспетчерами и механиками для планирования и выполнения работ."""
from datetime import datetime

from sqlalchemy import String, Text, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class RepairRequestOrm(BaseOrm):
    __tablename__ = "repair_requests"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"), index=True)
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String, index=True)
    priority: Mapped[str] = mapped_column(String, index=True)
    requested_by: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    approved_by: Mapped[str] = mapped_column(String, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, index=True)
    closed_at: Mapped[datetime] = mapped_column(DateTime, index=True)

    __table_args__ = (
        # Уникальная заявка на ремонт по машине, статусу и времени создания (исключает дубли в работе)
        UniqueConstraint("vehicle_id", "status", "created_at", name="uq_repair_vehicle_status_created"),
        # Индекс по авто и статусу — для фильтрации активных заявок
        Index("ix_repair_vehicle_status", "vehicle_id", "status"),
        # Индекс по дате закрытия — для аналитики выполнения ремонтов по периоду
        Index("ix_repair_closed", "closed_at"),
    )
