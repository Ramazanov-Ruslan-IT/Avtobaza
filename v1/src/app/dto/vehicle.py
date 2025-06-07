from dataclasses import dataclass

from v1.src.app.dto.base import BaseDTO


@dataclass
class VehicleDTO(BaseDTO):
    id: str | None = None
    license_plate: str | None = None
    brand: str | None = None
    model: str | None = None
    body_type: str | None = None
    vin: str | None = None
    fuel_type_id: int | None = None
    autobase_id: str | None = None
    status: str | None = None
    mileage: float | None = None
