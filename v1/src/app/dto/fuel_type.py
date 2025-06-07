from dataclasses import dataclass

from v1.src.app.dto.base import BaseDTO


@dataclass
class FuelTypeDTO(BaseDTO):
    id: int | None = None
    name: str | None = None
    octane_rating: int | None = None
    is_diesel: bool | None = None
