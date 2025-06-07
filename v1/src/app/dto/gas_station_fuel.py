from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class GasStationFuelDTO(BaseDTO):
    id: str | None = None
    gas_station_id: str | None = None
    fuel_type_id: int | None = None
    price_per_litre: float | None = None
    available: bool | None = None
    updated_at: datetime | None = None
