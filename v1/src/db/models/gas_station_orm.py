"""gas_stations - АЗС: название, адрес, координаты, статус (работает / на обслуживании). Используется в логике заправок, выбора маршрутов и аналитике."""

from sqlalchemy import String, Text, Float, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class GasStationOrm(BaseOrm):
    __tablename__ = "gas_stations"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(Text)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String)
