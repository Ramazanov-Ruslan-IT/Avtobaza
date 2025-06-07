from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class MlSuggestionDTO(BaseDTO):
    id: str | None = None
    suggestion_type: str | None = None
    target_entity: str | None = None
    entity_id: str | None = None
    message: str | None = None
    created_at: datetime | None = None
    resolved: bool | None = None
