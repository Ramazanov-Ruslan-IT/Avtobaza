from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class EfficiencyMetricDTO(BaseDTO):
    id: str | None = None
    vehicle_id: str | None = None
    date: datetime | None = None
    fuel_consumed: float | None = None
    km_travelled: float | None = None
    cost_per_km: float | None = None
    idle_time_minutes: int | None = None
