from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class RepairRequestDTO(BaseDTO):
    id: str | None = None
    vehicle_id: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None
    requested_by: str | None = None
    approved_by: str | None = None
    created_at: datetime | None = None
    closed_at: datetime | None = None
