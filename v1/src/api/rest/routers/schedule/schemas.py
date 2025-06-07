from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ScheduleCreateSchema(BaseModel):
    autobase_id: str
    vehicle_id: str
    task_type: str
    due_date: datetime
    status: str
    created_by: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ScheduleGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class ScheduleUpdateSchema(BaseModel):
    id: str
    autobase_id: str | None = None
    vehicle_id: str | None = None
    task_type: str | None = None
    due_date: datetime | None = None
    status: str | None = None
    created_by: str | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class ScheduleDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class ScheduleResponseSchema1(BaseModel):
    id: str
    autobase_id: str
    vehicle_id: str
    task_type: str
    due_date: datetime
    status: str
    created_by: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ScheduleResponseSchema2(ScheduleResponseSchema1): pass
class ScheduleResponseSchema3(ScheduleResponseSchema1): pass
class ScheduleResponseSchema4(ScheduleResponseSchema1): pass
