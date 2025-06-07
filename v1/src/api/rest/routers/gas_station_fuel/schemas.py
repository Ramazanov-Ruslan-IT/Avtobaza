from datetime import datetime
from pydantic import BaseModel, ConfigDict

class GasStationFuelCreateSchema(BaseModel):
    gas_station_id: str
    fuel_type_id: int
    price_per_litre: float
    available: bool
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class GasStationFuelGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class GasStationFuelUpdateSchema(BaseModel):
    id: str
    gas_station_id: str | None = None
    fuel_type_id: int | None = None
    price_per_litre: float | None = None
    available: bool | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class GasStationFuelDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class GasStationFuelResponseSchema1(BaseModel):
    id: str
    gas_station_id: str
    fuel_type_id: int
    price_per_litre: float
    available: bool
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class GasStationFuelResponseSchema2(GasStationFuelResponseSchema1): pass
class GasStationFuelResponseSchema3(GasStationFuelResponseSchema1): pass
class GasStationFuelResponseSchema4(GasStationFuelResponseSchema1): pass
