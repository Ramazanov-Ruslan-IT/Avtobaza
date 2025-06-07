from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class GpsTrackDTO(BaseDTO):
    id: str | None = None
    vehicle_id: str | None = None
    recorded_at: datetime | None = None
    latitude: float | None = None
    longitude: float | None = None
    speed_kmh: float | None = None
    event_type: str | None = None
