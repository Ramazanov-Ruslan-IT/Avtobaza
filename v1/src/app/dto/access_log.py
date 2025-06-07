from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class AccessLogDTO(BaseDTO):
    id: str | None = None
    user_id: str | None = None
    login_time: datetime | None = None
    logout_time: datetime | None = None
    ip_address: str | None = None
    user_agent: str | None = None
    successful: bool | None = None
