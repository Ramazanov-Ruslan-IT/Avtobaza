from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class ScheduleDTO(BaseDTO):
    id: str | None = None
    autobase_id: str | None = None
    vehicle_id: str | None = None
    task_type: str | None = None
    due_date: datetime | None = None
    status: str | None = None
    created_by: str | None = None
    created_at: datetime | None = None
