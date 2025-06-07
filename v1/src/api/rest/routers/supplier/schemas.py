from pydantic import BaseModel, ConfigDict

class SupplierCreateSchema(BaseModel):
    name: str
    contact_email: str
    phone: str
    address: str

    model_config = ConfigDict(from_attributes=True)

class SupplierGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class SupplierUpdateSchema(BaseModel):
    id: str
    name: str | None = None
    contact_email: str | None = None
    phone: str | None = None
    address: str | None = None

    model_config = ConfigDict(from_attributes=True)

class SupplierDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class SupplierResponseSchema1(BaseModel):
    id: str
    name: str
    contact_email: str
    phone: str
    address: str

    model_config = ConfigDict(from_attributes=True)

class SupplierResponseSchema2(SupplierResponseSchema1): pass
class SupplierResponseSchema3(SupplierResponseSchema1): pass
class SupplierResponseSchema4(SupplierResponseSchema1): pass
