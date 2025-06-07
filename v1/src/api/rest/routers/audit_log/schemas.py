from datetime import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict


class AuditLogCreateSchema(BaseModel):
    user_id: str
    action: str
    entity: str
    entity_id: str
    timestamp: datetime
    details: dict[str, Any]

    model_config = ConfigDict(from_attributes=True)


class AuditLogGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)


class AuditLogUpdateSchema(BaseModel):
    id: str
    user_id: str | None = None
    action: str | None = None
    entity: str | None = None
    entity_id: str | None = None
    timestamp: datetime | None = None
    details: dict[str, Any] | None = None

    model_config = ConfigDict(from_attributes=True)


class AuditLogDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)


class AuditLogResponseSchema1(BaseModel):
    id: str
    user_id: str
    action: str
    entity: str
    entity_id: str
    timestamp: datetime
    details: dict[str, Any]

    model_config = ConfigDict(from_attributes=True)


class AuditLogResponseSchema2(AuditLogResponseSchema1): pass
class AuditLogResponseSchema3(AuditLogResponseSchema1): pass
class AuditLogResponseSchema4(AuditLogResponseSchema1): pass
