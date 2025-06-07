from typing import List, Optional
from pydantic import BaseModel, ConfigDict

# --- CRUD-схемы ---
class VehicleCreateSchema(BaseModel):
    license_plate: str
    brand: str
    model: str
    body_type: str
    vin: str
    fuel_type_id: int
    autobase_id: str
    status: str
    mileage: float
    model_config = ConfigDict(from_attributes=True)

class VehicleGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class VehicleUpdateSchema(BaseModel):
    id: str
    license_plate: str | None = None
    brand: str | None = None
    model: str | None = None
    body_type: str | None = None
    vin: str | None = None
    fuel_type_id: int | None = None
    autobase_id: str | None = None
    status: str | None = None
    mileage: float | None = None
    model_config = ConfigDict(from_attributes=True)

class VehicleDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class VehicleResponseSchema1(BaseModel):
    id: str
    license_plate: str
    brand: str
    model: str
    body_type: str
    vin: str
    fuel_type_id: int
    autobase_id: str
    status: str
    mileage: float
    model_config = ConfigDict(from_attributes=True)

class VehicleResponseSchema2(VehicleResponseSchema1): pass
class VehicleResponseSchema3(VehicleResponseSchema1): pass
class VehicleResponseSchema4(VehicleResponseSchema1): pass

# --- Дополнительные схемы для расширенных endpoint-ов ---

# /vehicle/list и /vehicle/search
VehicleListSchema = List[VehicleResponseSchema1]

# /vehicle/history/{vehicle_id}
class VehicleHistoryEventSchema(BaseModel):
    event: str
    model_config = ConfigDict(from_attributes=True)

VehicleHistoryResponseSchema = List[VehicleHistoryEventSchema]

# /vehicle/assign-driver/{vehicle_id}
class AssignDriverRequestSchema(BaseModel):
    driver_id: str
    model_config = ConfigDict(from_attributes=True)

class AssignDriverResponseSchema(BaseModel):
    success: bool
    message: str
    model_config = ConfigDict(from_attributes=True)

# /vehicle/mileage/{vehicle_id}
class VehicleMileageResponseSchema(BaseModel):
    vehicle_id: str
    mileage: float
    model_config = ConfigDict(from_attributes=True)

# /vehicle/analytics
class FleetAnalyticsResponseSchema(BaseModel):
    avg_mileage: float
    max_mileage: float
    total_fuel_cost: float
    vehicles_in_service: int
    vehicles_under_repair: int
    model_config = ConfigDict(from_attributes=True)
