from datetime import datetime
from pydantic import BaseModel, ConfigDict

class MaintenanceLogCreateSchema(BaseModel):
    vehicle_id: str
    maintenance_type: str
    description: str
    cost: float
    performed_at: datetime
    mileage_at_maintenance: float
    user_id: str

    model_config = ConfigDict(from_attributes=True)

class MaintenanceLogGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class MaintenanceLogUpdateSchema(BaseModel):
    id: str
    vehicle_id: str | None = None
    maintenance_type: str | None = None
    description: str | None = None
    cost: float | None = None
    performed_at: datetime | None = None
    mileage_at_maintenance: float | None = None
    user_id: str | None = None

    model_config = ConfigDict(from_attributes=True)

class MaintenanceLogDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class MaintenanceLogResponseSchema1(BaseModel):
    id: str
    vehicle_id: str
    maintenance_type: str
    description: str
    cost: float
    performed_at: datetime
    mileage_at_maintenance: float
    user_id: str

    model_config = ConfigDict(from_attributes=True)

class MaintenanceLogResponseSchema2(MaintenanceLogResponseSchema1): pass
class MaintenanceLogResponseSchema3(MaintenanceLogResponseSchema1): pass
class MaintenanceLogResponseSchema4(MaintenanceLogResponseSchema1): pass
