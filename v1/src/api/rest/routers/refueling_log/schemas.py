from datetime import datetime
from pydantic import BaseModel, ConfigDict

class RefuelingLogCreateSchema(BaseModel):
    vehicle_id: str
    gas_station_id: str
    fuel_type_id: int
    litres: float
    total_cost: float
    refueled_at: datetime
    user_id: str
    mileage_at_refuel: float

    model_config = ConfigDict(from_attributes=True)

class RefuelingLogGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class RefuelingLogUpdateSchema(BaseModel):
    id: str
    vehicle_id: str | None = None
    gas_station_id: str | None = None
    fuel_type_id: int | None = None
    litres: float | None = None
    total_cost: float | None = None
    refueled_at: datetime | None = None
    user_id: str | None = None
    mileage_at_refuel: float | None = None

    model_config = ConfigDict(from_attributes=True)

class RefuelingLogDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class RefuelingLogResponseSchema1(BaseModel):
    id: str
    vehicle_id: str
    gas_station_id: str
    fuel_type_id: int
    litres: float
    total_cost: float
    refueled_at: datetime
    user_id: str
    mileage_at_refuel: float

    model_config = ConfigDict(from_attributes=True)

class RefuelingLogResponseSchema2(RefuelingLogResponseSchema1): pass
class RefuelingLogResponseSchema3(RefuelingLogResponseSchema1): pass
class RefuelingLogResponseSchema4(RefuelingLogResponseSchema1): pass
