from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class ScheduledTaskDTO(BaseDTO):
    id: str | None = None
    task_type: str | None = None
    target_entity: str | None = None
    entity_id: str | None = None
    cron_expression: str | None = None
    status: str | None = None
    last_run: datetime | None = None
    next_run: datetime | None = None
