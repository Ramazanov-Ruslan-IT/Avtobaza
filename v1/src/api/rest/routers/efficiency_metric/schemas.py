from datetime import datetime
from pydantic import BaseModel, ConfigDict

class EfficiencyMetricCreateSchema(BaseModel):
    vehicle_id: str
    date: datetime
    fuel_consumed: float
    km_travelled: float
    cost_per_km: float
    idle_time_minutes: int

    model_config = ConfigDict(from_attributes=True)

class EfficiencyMetricGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class EfficiencyMetricUpdateSchema(BaseModel):
    id: str
    vehicle_id: str | None = None
    date: datetime | None = None
    fuel_consumed: float | None = None
    km_travelled: float | None = None
    cost_per_km: float | None = None
    idle_time_minutes: int | None = None

    model_config = ConfigDict(from_attributes=True)

class EfficiencyMetricDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class EfficiencyMetricResponseSchema1(BaseModel):
    id: str
    vehicle_id: str
    date: datetime
    fuel_consumed: float
    km_travelled: float
    cost_per_km: float
    idle_time_minutes: int

    model_config = ConfigDict(from_attributes=True)

class EfficiencyMetricResponseSchema2(EfficiencyMetricResponseSchema1): pass
class EfficiencyMetricResponseSchema3(EfficiencyMetricResponseSchema1): pass
class EfficiencyMetricResponseSchema4(EfficiencyMetricResponseSchema1): pass
