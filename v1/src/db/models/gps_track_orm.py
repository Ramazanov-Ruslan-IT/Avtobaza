"""gps_tracks - Телеметрия: координаты, время, скорость, событие (например, резкое торможение). Используется для трекинга транспорта в реальном времени."""
from datetime import datetime

from sqlalchemy import String, Float, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class GpsTrackOrm(BaseOrm):
    __tablename__ = "gps_tracks"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"))
    recorded_at: Mapped[datetime] = mapped_column(DateTime)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    speed_kmh: Mapped[float] = mapped_column(Float)
    event_type: Mapped[str] = mapped_column(String)
