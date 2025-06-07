from datetime import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict

class ReportCreateSchema(BaseModel):
    type: str
    created_by: str
    generated_at: datetime
    payload: dict[str, Any]

    model_config = ConfigDict(from_attributes=True)

class ReportGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class ReportUpdateSchema(BaseModel):
    id: str
    type: str | None = None
    created_by: str | None = None
    generated_at: datetime | None = None
    payload: dict[str, Any] | None = None

    model_config = ConfigDict(from_attributes=True)

class ReportDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class ReportResponseSchema1(BaseModel):
    id: str
    type: str
    created_by: str
    generated_at: datetime
    payload: dict[str, Any]

    model_config = ConfigDict(from_attributes=True)

class ReportResponseSchema2(ReportResponseSchema1): pass
class ReportResponseSchema3(ReportResponseSchema1): pass
class ReportResponseSchema4(ReportResponseSchema1): pass
