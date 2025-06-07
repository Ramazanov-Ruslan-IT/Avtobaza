from datetime import datetime
from pydantic import BaseModel, ConfigDict

class FinancialTransactionCreateSchema(BaseModel):
    transaction_type: str
    category: str
    amount: float
    currency: str
    date: datetime
    vehicle_id: str
    user_id: str
    description: str

    model_config = ConfigDict(from_attributes=True)

class FinancialTransactionGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class FinancialTransactionUpdateSchema(BaseModel):
    id: str
    transaction_type: str | None = None
    category: str | None = None
    amount: float | None = None
    currency: str | None = None
    date: datetime | None = None
    vehicle_id: str | None = None
    user_id: str | None = None
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)

class FinancialTransactionDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class FinancialTransactionResponseSchema1(BaseModel):
    id: str
    transaction_type: str
    category: str
    amount: float
    currency: str
    date: datetime
    vehicle_id: str
    user_id: str
    description: str

    model_config = ConfigDict(from_attributes=True)

class FinancialTransactionResponseSchema2(FinancialTransactionResponseSchema1): pass
class FinancialTransactionResponseSchema3(FinancialTransactionResponseSchema1): pass
class FinancialTransactionResponseSchema4(FinancialTransactionResponseSchema1): pass
