from datetime import datetime
from pydantic import BaseModel, ConfigDict

class StorageFuelCreateSchema(BaseModel):
    autobase_id: str
    fuel_type_id: int
    litres: float
    last_updated: datetime

    model_config = ConfigDict(from_attributes=True)

class StorageFuelGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class StorageFuelUpdateSchema(BaseModel):
    id: str
    autobase_id: str | None = None
    fuel_type_id: int | None = None
    litres: float | None = None
    last_updated: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class StorageFuelDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class StorageFuelResponseSchema1(BaseModel):
    id: str
    autobase_id: str
    fuel_type_id: int
    litres: float
    last_updated: datetime

    model_config = ConfigDict(from_attributes=True)

class StorageFuelResponseSchema2(StorageFuelResponseSchema1): pass
class StorageFuelResponseSchema3(StorageFuelResponseSchema1): pass
class StorageFuelResponseSchema4(StorageFuelResponseSchema1): pass
