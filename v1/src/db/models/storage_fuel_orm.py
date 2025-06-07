"""storage_fuel - Остатки топлива на складе автобазы: сорт, объём, время последнего обновления. Нужно, если у предприятия есть собственные заправки или хранение топлива."""
from datetime import datetime

from sqlalchemy import String, Float, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class StorageFuelOrm(BaseOrm):
    __tablename__ = "storage_fuel"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    autobase_id: Mapped[str] = mapped_column(ForeignKey("autobases.id"))
    fuel_type_id: Mapped[int] = mapped_column(ForeignKey("fuel_types.id"))
    litres: Mapped[float] = mapped_column(Float)
    last_updated: Mapped[datetime] = mapped_column(DateTime)
