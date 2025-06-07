from dataclasses import dataclass

from v1.src.app.dto.base import BaseDTO


@dataclass
class GasStationDTO(BaseDTO):
    id: str | None = None
    name: str | None = None
    address: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    status: str | None = None
