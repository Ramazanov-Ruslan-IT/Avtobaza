from datetime import datetime
from pydantic import BaseModel, ConfigDict


class AccessLogCreateSchema(BaseModel):
    user_id: str
    login_time: datetime
    logout_time: datetime | None = None
    ip_address: str
    user_agent: str
    successful: bool

    model_config = ConfigDict(from_attributes=True)


class AccessLogGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)


class AccessLogUpdateSchema(BaseModel):
    id: str
    user_id: str | None = None
    login_time: datetime | None = None
    logout_time: datetime | None = None
    ip_address: str | None = None
    user_agent: str | None = None
    successful: bool | None = None

    model_config = ConfigDict(from_attributes=True)


class AccessLogDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)


class AccessLogResponseSchema1(BaseModel):
    id: str
    user_id: str
    login_time: datetime
    logout_time: datetime | None = None
    ip_address: str
    user_agent: str
    successful: bool

    model_config = ConfigDict(from_attributes=True)


class AccessLogResponseSchema2(AccessLogResponseSchema1): pass
class AccessLogResponseSchema3(AccessLogResponseSchema1): pass
class AccessLogResponseSchema4(AccessLogResponseSchema1): pass
