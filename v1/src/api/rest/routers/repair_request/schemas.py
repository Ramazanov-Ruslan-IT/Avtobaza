from datetime import datetime
from pydantic import BaseModel, ConfigDict

# CRUD

class RepairRequestCreateSchema(BaseModel):
    vehicle_id: str
    description: str
    status: str
    priority: str
    requested_by: str
    approved_by: str
    created_at: datetime
    closed_at: datetime
    model_config = ConfigDict(from_attributes=True)

class RepairRequestGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class RepairRequestUpdateSchema(BaseModel):
    id: str
    vehicle_id: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None
    requested_by: str | None = None
    approved_by: str | None = None
    created_at: datetime | None = None
    closed_at: datetime | None = None
    model_config = ConfigDict(from_attributes=True)

class RepairRequestDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class RepairRequestResponseSchema1(BaseModel):
    id: str
    vehicle_id: str
    description: str
    status: str
    priority: str
    requested_by: str
    approved_by: str
    created_at: datetime
    closed_at: datetime
    model_config = ConfigDict(from_attributes=True)

class RepairRequestResponseSchema2(RepairRequestResponseSchema1): pass
class RepairRequestResponseSchema3(RepairRequestResponseSchema1): pass
class RepairRequestResponseSchema4(RepairRequestResponseSchema1): pass

# --- Расширенные схемы ---

# Список заявок (например, фильтрация по статусу)
RepairRequestListSchema = list[RepairRequestResponseSchema1]

# Массовое обновление статусов (batch approve/close)
class RepairRequestBatchStatusSchema(BaseModel):
    ids: list[str]
    status: str
    model_config = ConfigDict(from_attributes=True)
RepairRequestBatchStatusResponseSchema = list[RepairRequestResponseSchema1]

# История изменений по заявке (timeline)
class RepairRequestHistoryEventSchema(BaseModel):
    timestamp: datetime
    status: str
    comment: str | None = None
    model_config = ConfigDict(from_attributes=True)
RepairRequestHistoryListSchema = list[RepairRequestHistoryEventSchema]

# Статистика по заявкам
class RepairRequestStatsSchema(BaseModel):
    total: int
    open: int
    closed: int
    urgent: int
    avg_close_time_hours: float
    model_config = ConfigDict(from_attributes=True)
