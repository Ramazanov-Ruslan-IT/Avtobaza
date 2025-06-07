from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class AuditLogDTO(BaseDTO):
    id: str | None = None
    user_id: str | None = None
    action: str | None = None
    entity: str | None = None
    entity_id: str | None = None
    timestamp: datetime | None = None
    details: dict | None = None
