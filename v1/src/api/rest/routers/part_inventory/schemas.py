from datetime import datetime
from pydantic import BaseModel, ConfigDict

class PartInventoryCreateSchema(BaseModel):
    name: str
    part_number: str
    category: str
    unit: str
    quantity: int
    reorder_threshold: int
    last_updated: datetime
    supplier_id: str

    model_config = ConfigDict(from_attributes=True)

class PartInventoryGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class PartInventoryUpdateSchema(BaseModel):
    id: str
    name: str | None = None
    part_number: str | None = None
    category: str | None = None
    unit: str | None = None
    quantity: int | None = None
    reorder_threshold: int | None = None
    last_updated: datetime | None = None
    supplier_id: str | None = None

    model_config = ConfigDict(from_attributes=True)

class PartInventoryDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class PartInventoryResponseSchema1(BaseModel):
    id: str
    name: str
    part_number: str
    category: str
    unit: str
    quantity: int
    reorder_threshold: int
    last_updated: datetime
    supplier_id: str

    model_config = ConfigDict(from_attributes=True)

class PartInventoryResponseSchema2(PartInventoryResponseSchema1): pass
class PartInventoryResponseSchema3(PartInventoryResponseSchema1): pass
class PartInventoryResponseSchema4(PartInventoryResponseSchema1): pass
