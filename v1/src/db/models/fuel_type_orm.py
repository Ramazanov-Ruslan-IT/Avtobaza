"""fuel_types - Справочник видов топлива: АИ-92, АИ-95, ДТ и др. Указывает октановое число, дизельное ли. Применяется во всех операциях с топливом."""

from sqlalchemy import Integer, String, Boolean, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class FuelTypeOrm(BaseOrm):
    __tablename__ = "fuel_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    octane_rating: Mapped[int] = mapped_column(Integer, index=True)
    is_diesel: Mapped[bool] = mapped_column(Boolean, index=True)

    __table_args__ = (
        # Гарантирует, что не будет дубля по названию и октановому числу
        UniqueConstraint("name", "octane_rating", name="uq_fueltype_name_octane"),
        # Индекс для поиска всех типов топлива по дизельности и октановому числу
        Index("ix_fueltype_diesel_octane", "is_diesel", "octane_rating"),
    )
