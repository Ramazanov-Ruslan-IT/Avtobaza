from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class PartInventoryDTO(BaseDTO):
    id: str | None = None
    name: str | None = None
    part_number: str | None = None
    category: str | None = None
    unit: str | None = None
    quantity: int | None = None
    reorder_threshold: int | None = None
    last_updated: datetime | None = None
    supplier_id: str | None = None
