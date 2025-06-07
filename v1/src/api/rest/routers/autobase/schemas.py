from pydantic import BaseModel, ConfigDict

class AutobaseCreateSchema(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float

    model_config = ConfigDict(from_attributes=True)

class AutobaseGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class AutobaseUpdateSchema(BaseModel):
    id: str
    name: str | None = None
    address: str | None = None
    latitude: float | None = None
    longitude: float | None = None

    model_config = ConfigDict(from_attributes=True)

class AutobaseDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class AutobaseResponseSchema1(BaseModel):
    id: str
    name: str
    address: str
    latitude: float
    longitude: float

    model_config = ConfigDict(from_attributes=True)

class AutobaseResponseSchema2(AutobaseResponseSchema1): pass
class AutobaseResponseSchema3(AutobaseResponseSchema1): pass
class AutobaseResponseSchema4(AutobaseResponseSchema1): pass
