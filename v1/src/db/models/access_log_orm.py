"""access_logs - Фиксирует все попытки входа в систему: время входа/выхода, IP, устройство, успешность. Используется для безопасности и расследований."""
from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class AccessLogOrm(BaseOrm):
    __tablename__ = "access_logs"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    login_time: Mapped[datetime] = mapped_column(DateTime)
    logout_time: Mapped[datetime] = mapped_column(DateTime)
    ip_address: Mapped[str] = mapped_column(String)
    user_agent: Mapped[str] = mapped_column(String)
    successful: Mapped[bool] = mapped_column(Boolean)
