"""audit_logs - Аудит действий пользователей: кто, что, когда изменил. Хранит сущность, ID, время, детали. Используется для контроля и расследований."""
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, JSON, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class AuditLogOrm(BaseOrm):
    __tablename__ = "audit_logs"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    action: Mapped[str] = mapped_column(String)
    entity: Mapped[str] = mapped_column(String)
    entity_id: Mapped[str] = mapped_column(String)
    timestamp: Mapped[datetime] = mapped_column(DateTime)
    details: Mapped[dict] = mapped_column(JSON)
