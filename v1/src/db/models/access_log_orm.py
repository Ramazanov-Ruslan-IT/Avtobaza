"""access_logs - Фиксирует все попытки входа в систему: время входа/выхода, IP, устройство, успешность. Используется для безопасности и расследований."""
from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class AccessLogOrm(BaseOrm):
    __tablename__ = "access_logs"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    login_time: Mapped[datetime] = mapped_column(DateTime, index=True)
    logout_time: Mapped[datetime] = mapped_column(DateTime)
    ip_address: Mapped[str] = mapped_column(String, index=True)
    user_agent: Mapped[str] = mapped_column(String)
    successful: Mapped[bool] = mapped_column(Boolean, index=True)

    __table_args__ = (
        # Композитный индекс: быстрый поиск всех попыток авторизации пользователя за период с конкретного IP
        Index("ix_access_logs_userid_ip", "user_id", "ip_address"),
        # Композитный индекс: все входы/выходы пользователя по успешности за период (для анализа атак/подбора)
        Index("ix_access_logs_user_successful", "user_id", "successful", "login_time"),
        # Частичный индекс (PostgreSQL): ускоряет анализ неудачных попыток входа (попытки взлома)
        Index("ix_access_logs_failed_logins", "user_id", "login_time",
              postgresql_where=(successful == False)),
    )
