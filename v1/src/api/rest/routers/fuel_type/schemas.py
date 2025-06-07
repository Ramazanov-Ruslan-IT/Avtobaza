from pydantic import BaseModel, ConfigDict

class FuelTypeCreateSchema(BaseModel):
    name: str
    octane_rating: int
    is_diesel: bool

    model_config = ConfigDict(from_attributes=True)

class FuelTypeGetSchema(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)

class FuelTypeUpdateSchema(BaseModel):
    id: int
    name: str | None = None
    octane_rating: int | None = None
    is_diesel: bool | None = None

    model_config = ConfigDict(from_attributes=True)

class FuelTypeDeleteSchema(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)

class FuelTypeResponseSchema1(BaseModel):
    id: int
    name: str
    octane_rating: int
    is_diesel: bool

    model_config = ConfigDict(from_attributes=True)

class FuelTypeResponseSchema2(FuelTypeResponseSchema1): pass
class FuelTypeResponseSchema3(FuelTypeResponseSchema1): pass
class FuelTypeResponseSchema4(FuelTypeResponseSchema1): pass
