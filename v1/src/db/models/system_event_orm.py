"""system_events - Системные события: ошибки, падения, технические логи. Полезны для админов и отладки."""
from datetime import datetime

from sqlalchemy import String, Text, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class SystemEventOrm(BaseOrm):
    __tablename__ = "system_events"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    level: Mapped[str] = mapped_column(String, index=True)
    source_module: Mapped[str] = mapped_column(String, index=True)
    message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, index=True)
    trace_id: Mapped[str] = mapped_column(String, index=True)

    __table_args__ = (
        # Композитный индекс для анализа событий по уровню, времени и модулю
        Index("ix_systemevent_level_module_time", "level", "source_module", "created_at"),
        # Индекс по trace_id — чтобы быстро найти все логи одного запроса/трейса
        Index("ix_systemevent_traceid", "trace_id"),
    )
