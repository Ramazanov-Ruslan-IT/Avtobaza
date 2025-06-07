"""routes - Маршруты, по которым двигались автомобили. Содержит начальную и конечную точку, маршрут в формате JSON, километраж, водителя. Используется в логистике и аналитике."""
from datetime import datetime

from sqlalchemy import String, Float, DateTime, ForeignKey, JSON, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from v1.src.db.models.base_orm import BaseOrm


class RouteOrm(BaseOrm):
    __tablename__ = "routes"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_id: Mapped[str] = mapped_column(ForeignKey("vehicles.id"))
    origin: Mapped[str] = mapped_column(String)
    destination: Mapped[str] = mapped_column(String)
    route_data: Mapped[dict] = mapped_column(JSON)
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    distance_km: Mapped[float] = mapped_column(Float)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
