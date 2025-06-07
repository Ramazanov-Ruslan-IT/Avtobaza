"""schedules - Плановые задания: ТО, проверки, замена масла и т.п. Содержит дату, статус, кто создал. Используется для регулярного обслуживания."""
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class ScheduleOrm(BaseOrm):
    __tablename__ = "schedules"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    autobase_id: Mapped[str] = mapped_column(ForeignKey("autobases.id"), index=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"), index=True)
    task_type: Mapped[str] = mapped_column(String, index=True)
    due_date: Mapped[datetime] = mapped_column(DateTime, index=True)
    status: Mapped[str] = mapped_column(String, index=True)
    created_by: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, index=True)

    __table_args__ = (
        # Уникальное задание на авто по типу и сроку — чтобы не было дублей ТО, замен и пр.
        UniqueConstraint("vehicle_id", "task_type", "due_date", name="uq_schedule_vehicle_task_date"),
        # Индекс для фильтрации заданий по базе и дате (например, все задания на месяц по базе)
        Index("ix_schedule_autobase_date", "autobase_id", "due_date"),
        # Индекс для поиска заданий по статусу (активные, просроченные, выполненные)
        Index("ix_schedule_status_due", "status", "due_date"),
    )
