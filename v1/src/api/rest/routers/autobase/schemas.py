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
# Список автобаз
AutobaseListSchema = list[AutobaseResponseSchema1]

# Поиск по имени/адресу/координатам
class AutobaseSearchSchema(BaseModel):
    name: str | None = None
    address: str | None = None
    lat_from: float | None = None
    lat_to: float | None = None
    lon_from: float | None = None
    lon_to: float | None = None
    model_config = ConfigDict(from_attributes=True)
AutobaseSearchListSchema = list[AutobaseResponseSchema1]

# Статистика по автобазе
class AutobaseStatsSchema(BaseModel):
    id: str
    name: str
    vehicles_count: int
    storage_fuel_litres: float
    open_repairs: int
    model_config = ConfigDict(from_attributes=True)
AutobaseStatsListSchema = list[AutobaseStatsSchema]