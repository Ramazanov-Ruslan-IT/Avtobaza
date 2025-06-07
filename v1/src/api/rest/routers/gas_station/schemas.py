from pydantic import BaseModel, ConfigDict

class GasStationCreateSchema(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
    status: str

    model_config = ConfigDict(from_attributes=True)

class GasStationGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class GasStationUpdateSchema(BaseModel):
    id: str
    name: str | None = None
    address: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    status: str | None = None

    model_config = ConfigDict(from_attributes=True)

class GasStationDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class GasStationResponseSchema1(BaseModel):
    id: str
    name: str
    address: str
    latitude: float
    longitude: float
    status: str

    model_config = ConfigDict(from_attributes=True)

class GasStationResponseSchema2(GasStationResponseSchema1): pass
class GasStationResponseSchema3(GasStationResponseSchema1): pass
class GasStationResponseSchema4(GasStationResponseSchema1): pass
