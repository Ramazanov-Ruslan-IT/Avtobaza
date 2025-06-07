from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class DocumentDTO(BaseDTO):
    id: str | None = None
    vehicle_id: str | None = None
    doc_type: str | None = None
    file_url: str | None = None
    uploaded_by: str | None = None
    uploaded_at: datetime | None = None
