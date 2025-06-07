from pydantic import BaseModel, ConfigDict

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
