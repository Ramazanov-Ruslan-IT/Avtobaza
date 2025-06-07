"""scheduled_tasks - Системные задачи: очистка логов, автосоздание отчётов, резервное копирование. Использует cron-подобный формат расписания."""
from datetime import datetime

from sqlalchemy import String, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class ScheduledTaskOrm(BaseOrm):
    __tablename__ = "scheduled_tasks"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    task_type: Mapped[str] = mapped_column(String, index=True)
    target_entity: Mapped[str] = mapped_column(String, index=True)
    entity_id: Mapped[str] = mapped_column(String, index=True)
    cron_expression: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String, index=True)
    last_run: Mapped[datetime] = mapped_column(DateTime, index=True)
    next_run: Mapped[datetime] = mapped_column(DateTime, index=True)

    __table_args__ = (
        # Уникальность системной задачи на конкретный объект, тип и расписание
        UniqueConstraint("task_type", "target_entity", "entity_id", "cron_expression", name="uq_schedtask_type_entity_cron"),
        # Индекс для поиска задач по статусу и времени следующего запуска
        Index("ix_schedtask_status_nextrun", "status", "next_run"),
    )
