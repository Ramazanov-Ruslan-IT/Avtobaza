from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class RefuelingLogDTO(BaseDTO):
    id: str | None = None
    vehicle_id: str | None = None
    gas_station_id: str | None = None
    fuel_type_id: int | None = None
    litres: float | None = None
    total_cost: float | None = None
    refueled_at: datetime | None = None
    user_id: str | None = None
    mileage_at_refuel: float | None = None
