"""gas_stations - АЗС: название, адрес, координаты, статус (работает / на обслуживании). Используется в логике заправок, выбора маршрутов и аналитике."""

from sqlalchemy import String, Text, Float, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class GasStationOrm(BaseOrm):
    __tablename__ = "gas_stations"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    address: Mapped[str] = mapped_column(Text)
    latitude: Mapped[float] = mapped_column(Float, index=True)
    longitude: Mapped[float] = mapped_column(Float, index=True)
    status: Mapped[str] = mapped_column(String, index=True)

    __table_args__ = (
        # Уникальная станция по имени и адресу (чтобы избежать дублей)
        UniqueConstraint("name", "address", name="uq_gasstation_name_address"),
        # Индекс для поиска по геолокации (например, для поиска ближайшей станции)
        Index("ix_gasstation_lat_lon", "latitude", "longitude"),
        # Индекс для фильтрации по статусу (работает/не работает)
        Index("ix_gasstation_status", "status"),
    )
