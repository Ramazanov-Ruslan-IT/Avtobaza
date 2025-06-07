from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class ReportDTO(BaseDTO):
    id: str | None = None
    type: str | None = None
    created_by: str | None = None
    generated_at: datetime | None = None
    payload: dict | None = None
