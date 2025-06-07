from datetime import datetime
from pydantic import BaseModel, ConfigDict

class SystemEventCreateSchema(BaseModel):
    level: str
    source_module: str
    message: str
    created_at: datetime
    trace_id: str

    model_config = ConfigDict(from_attributes=True)

class SystemEventGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class SystemEventUpdateSchema(BaseModel):
    id: str
    level: str | None = None
    source_module: str | None = None
    message: str | None = None
    created_at: datetime | None = None
    trace_id: str | None = None

    model_config = ConfigDict(from_attributes=True)

class SystemEventDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class SystemEventResponseSchema1(BaseModel):
    id: str
    level: str
    source_module: str
    message: str
    created_at: datetime
    trace_id: str

    model_config = ConfigDict(from_attributes=True)

class SystemEventResponseSchema2(SystemEventResponseSchema1): pass
class SystemEventResponseSchema3(SystemEventResponseSchema1): pass
class SystemEventResponseSchema4(SystemEventResponseSchema1): pass
