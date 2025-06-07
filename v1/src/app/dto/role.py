from dataclasses import dataclass

from v1.src.app.dto.base import BaseDTO


@dataclass
class RoleDTO(BaseDTO):
    id: int | None = None
    name: str | None = None
    description: str | None = None
