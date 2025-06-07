"""audit_logs - Аудит действий пользователей: кто, что, когда изменил. Хранит сущность, ID, время, детали. Используется для контроля и расследований."""
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, JSON, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class AuditLogOrm(BaseOrm):
    __tablename__ = "audit_logs"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    action: Mapped[str] = mapped_column(String, index=True)
    entity: Mapped[str] = mapped_column(String, index=True)
    entity_id: Mapped[str] = mapped_column(String, index=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime, index=True)
    details: Mapped[dict] = mapped_column(JSON)

    __table_args__ = (
        Index("ix_audit_entity_object", "entity", "entity_id"),
        Index("ix_audit_user_time", "user_id", "timestamp"),
        Index("ix_audit_action_entity", "action", "entity", "entity_id"),
    )
