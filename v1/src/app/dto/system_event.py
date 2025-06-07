from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class SystemEventDTO(BaseDTO):
    id: str | None = None
    level: str | None = None
    source_module: str | None = None
    message: str | None = None
    created_at: datetime | None = None
    trace_id: str | None = None
