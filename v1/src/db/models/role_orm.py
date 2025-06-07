"""roles - Справочник ролей: администратор, диспетчер, механик, водитель и др. С ним связана таблица users. Позволяет ограничивать доступ к функциям."""

from sqlalchemy import Integer, String, Text, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from v1.src.db.models.base_orm import BaseOrm


class RoleOrm(BaseOrm):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(Text)

    users = relationship("UserOrm", back_populates="role")

    __table_args__ = (
        # Уникальность по названию роли — двух одинаковых быть не должно
        UniqueConstraint("name", name="uq_role_name"),
    )
