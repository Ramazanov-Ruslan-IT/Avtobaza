"""schedules - Плановые задания: ТО, проверки, замена масла и т.п. Содержит дату, статус, кто создал. Используется для регулярного обслуживания."""
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class ScheduleOrm(BaseOrm):
    __tablename__ = "schedules"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    autobase_id: Mapped[str] = mapped_column(ForeignKey("autobases.id"))
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"))
    task_type: Mapped[str] = mapped_column(String)
    due_date: Mapped[datetime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String)
    created_by: Mapped[str] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime)
