from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class RouteDTO(BaseDTO):
    id: str | None = None
    vehicle_id: str | None = None
    origin: str | None = None
    destination: str | None = None
    route_data: dict | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    distance_km: float | None = None
    user_id: str | None = None
