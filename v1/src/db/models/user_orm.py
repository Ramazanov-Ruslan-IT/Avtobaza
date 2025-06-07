"""users - Содержит данные зарегистрированных пользователей системы: email, ФИО, хеш пароля, роль, дата регистрации. Используется для авторизации, разграничения доступа и аудита действий."""

from sqlalchemy import String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from v1.src.db.models.base_orm import BaseOrm


class UserOrm(BaseOrm):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    email: Mapped[str] = mapped_column(String, index=True)
    full_name: Mapped[str] = mapped_column(String)
    password_hash: Mapped[str] = mapped_column(String)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), index=True)

    role = relationship("RoleOrm", back_populates="users")
