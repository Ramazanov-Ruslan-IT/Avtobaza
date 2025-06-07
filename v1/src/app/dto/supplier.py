from dataclasses import dataclass

from v1.src.app.dto.base import BaseDTO


@dataclass
class SupplierDTO(BaseDTO):
    id: str | None = None
    name: str | None = None
    contact_email: str | None = None
    phone: str | None = None
    address: str | None = None
