"""routes - Маршруты, по которым двигались автомобили. Содержит начальную и конечную точку, маршрут в формате JSON, километраж, водителя. Используется в логистике и аналитике."""
from datetime import datetime

from sqlalchemy import String, Float, DateTime, ForeignKey, JSON, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class RouteOrm(BaseOrm):
    __tablename__ = "routes"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"), index=True)
    origin: Mapped[str] = mapped_column(String, index=True)
    destination: Mapped[str] = mapped_column(String, index=True)
    route_data: Mapped[dict] = mapped_column(JSON)
    start_time: Mapped[datetime] = mapped_column(DateTime, index=True)
    end_time: Mapped[datetime] = mapped_column(DateTime, index=True)
    distance_km: Mapped[float] = mapped_column(Float)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)

    __table_args__ = (
        # Уникальный маршрут на одно авто с точками и временем старта
        UniqueConstraint("vehicle_id", "origin", "destination", "start_time", name="uq_route_vehicle_origin_dest_start"),
        # Индекс для анализа всех маршрутов авто по времени
        Index("ix_route_vehicle_time", "vehicle_id", "start_time", "end_time"),
        # Индекс для поиска маршрутов водителя за период
        Index("ix_route_user_time", "user_id", "start_time"),
    )
