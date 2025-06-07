from dataclasses import dataclass

from v1.src.app.dto.base import BaseDTO


@dataclass
class UserDTO(BaseDTO):
    id: str | None = None
    email: str | None = None
    full_name: str | None = None
    password_hash: str | None = None
    role_id: int | None = None
