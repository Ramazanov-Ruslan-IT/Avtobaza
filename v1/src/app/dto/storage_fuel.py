from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class StorageFuelDTO(BaseDTO):
    id: str | None = None
    autobase_id: str | None = None
    fuel_type_id: int | None = None
    litres: float | None = None
    last_updated: datetime | None = None
