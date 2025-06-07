from datetime import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict

class RouteCreateSchema(BaseModel):
    vehicle_id: str
    origin: str
    destination: str
    route_data: dict[str, Any]
    start_time: datetime
    end_time: datetime
    distance_km: float
    user_id: str

    model_config = ConfigDict(from_attributes=True)

class RouteGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class RouteUpdateSchema(BaseModel):
    id: str
    vehicle_id: str | None = None
    origin: str | None = None
    destination: str | None = None
    route_data: dict[str, Any] | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    distance_km: float | None = None
    user_id: str | None = None

    model_config = ConfigDict(from_attributes=True)

class RouteDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class RouteResponseSchema1(BaseModel):
    id: str
    vehicle_id: str
    origin: str
    destination: str
    route_data: dict[str, Any]
    start_time: datetime
    end_time: datetime
    distance_km: float
    user_id: str

    model_config = ConfigDict(from_attributes=True)

class RouteResponseSchema2(RouteResponseSchema1): pass
class RouteResponseSchema3(RouteResponseSchema1): pass
class RouteResponseSchema4(RouteResponseSchema1): pass
