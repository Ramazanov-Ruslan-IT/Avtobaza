"""system_events - Системные события: ошибки, падения, технические логи. Полезны для админов и отладки."""
from datetime import datetime

from sqlalchemy import String, Text, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class SystemEventOrm(BaseOrm):
    __tablename__ = "system_events"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    level: Mapped[str] = mapped_column(String)
    source_module: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    trace_id: Mapped[str] = mapped_column(String)
