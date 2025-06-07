"""gas_station_fuel - Наличие и цены топлива на каждой АЗС. Показывает, доступен ли нужный сорт топлива и по какой цене. Обновляется регулярно."""
from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, ForeignKey, Numeric, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class GasStationFuelOrm(BaseOrm):
    __tablename__ = "gas_station_fuel"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    gas_station_id: Mapped[str] = mapped_column(ForeignKey("gas_stations.id"), index=True)
    fuel_type_id: Mapped[int] = mapped_column(ForeignKey("fuel_types.id"), index=True)
    price_per_litre: Mapped[float] = mapped_column(Numeric)
    available: Mapped[bool] = mapped_column(Boolean)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
