from dataclasses import dataclass
from datetime import datetime

from v1.src.app.dto.base import BaseDTO


@dataclass
class FinancialTransactionDTO(BaseDTO):
    id: str | None = None
    transaction_type: str | None = None
    category: str | None = None
    amount: float | None = None
    currency: str | None = None
    date: datetime | None = None
    vehicle_id: str | None = None
    user_id: str | None = None
    description: str | None = None
