from datetime import datetime
from pydantic import BaseModel, ConfigDict

# --- CRUD-схемы ---

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


# Для списка остатков
StorageFuelListSchema = list[StorageFuelResponseSchema1]

# Для поиска по складу/типу топлива
class StorageFuelSearchSchema(BaseModel):
    autobase_id: str | None = None
    fuel_type_id: int | None = None
    model_config = ConfigDict(from_attributes=True)

StorageFuelSearchListSchema = list[StorageFuelResponseSchema1]

# Для статистики остатков по складам
class StorageFuelStatsSchema(BaseModel):
    autobase_id: str
    total_litres: float
    last_update: datetime
    model_config = ConfigDict(from_attributes=True)

StorageFuelStatsListSchema = list[StorageFuelStatsSchema]
