"""gps_tracks - Телеметрия: координаты, время, скорость, событие (например, резкое торможение). Используется для трекинга транспорта в реальном времени."""
from datetime import datetime

from sqlalchemy import String, Float, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class GpsTrackOrm(BaseOrm):
    __tablename__ = "gps_tracks"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"), index=True)
    recorded_at: Mapped[datetime] = mapped_column(DateTime, index=True)
    latitude: Mapped[float] = mapped_column(Float, index=True)
    longitude: Mapped[float] = mapped_column(Float, index=True)
    speed_kmh: Mapped[float] = mapped_column(Float)
    event_type: Mapped[str] = mapped_column(String, index=True)

    __table_args__ = (
        # Уникальное ограничение: для одного авто запись телеметрии за один момент времени только одна
        UniqueConstraint("vehicle_id", "recorded_at", name="uq_gpstrack_vehicle_time"),
        # Композитный индекс для быстрой выборки по авто и времени (например, трек за период)
        Index("ix_gpstrack_vehicle_time", "vehicle_id", "recorded_at"),
        # Индекс для поиска событий по координатам
        Index("ix_gpstrack_lat_lon", "latitude", "longitude"),
        # Индекс для поиска по типу события (например, экстренное торможение)
        Index("ix_gpstrack_event_type", "event_type"),
    )
