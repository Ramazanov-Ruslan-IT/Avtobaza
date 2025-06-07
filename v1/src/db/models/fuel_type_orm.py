"""fuel_types - Справочник видов топлива: АИ-92, АИ-95, ДТ и др. Указывает октановое число, дизельное ли. Применяется во всех операциях с топливом."""

from sqlalchemy import Integer, String, Boolean, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class FuelTypeOrm(BaseOrm):
    __tablename__ = "fuel_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    octane_rating: Mapped[int] = mapped_column(Integer)
    is_diesel: Mapped[bool] = mapped_column(Boolean)
