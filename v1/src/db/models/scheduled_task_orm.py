"""scheduled_tasks - Системные задачи: очистка логов, автосоздание отчётов, резервное копирование. Использует cron-подобный формат расписания."""
from datetime import datetime

from sqlalchemy import String, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class ScheduledTaskOrm(BaseOrm):
    __tablename__ = "scheduled_tasks"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    task_type: Mapped[str] = mapped_column(String)
    target_entity: Mapped[str] = mapped_column(String)
    entity_id: Mapped[str] = mapped_column(String)
    cron_expression: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    last_run: Mapped[datetime] = mapped_column(DateTime)
    next_run: Mapped[datetime] = mapped_column(DateTime)
