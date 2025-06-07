from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class GasStationContractDTO(BaseDTO):
    id: str | None = None
    autobase_id: str | None = None
    gas_station_id: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    terms: str | None = None
