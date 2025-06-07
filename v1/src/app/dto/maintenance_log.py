from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class MaintenanceLogDTO(BaseDTO):
    id: str | None = None
    vehicle_id: str | None = None
    maintenance_type: str | None = None
    description: str | None = None
    cost: float | None = None
    performed_at: datetime | None = None
    mileage_at_maintenance: float | None = None
    user_id: str | None = None
