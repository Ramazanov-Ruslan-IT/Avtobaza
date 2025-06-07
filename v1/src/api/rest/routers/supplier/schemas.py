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

# Список поставщиков (list)
SupplierListSchema = list[SupplierResponseSchema1]

# Массовое создание/обновление/удаление
class SupplierBatchOperationSchema(BaseModel):
    suppliers: list[SupplierCreateSchema]
    model_config = ConfigDict(from_attributes=True)

class SupplierBatchDeleteSchema(BaseModel):
    ids: list[str]
    model_config = ConfigDict(from_attributes=True)

# Поиск по части имени/email
class SupplierSearchResponseSchema(SupplierResponseSchema1): pass
SupplierSearchListSchema = list[SupplierSearchResponseSchema]

# Запрос всех email поставщиков
class SupplierEmailResponseSchema(BaseModel):
    contact_email: str
    model_config = ConfigDict(from_attributes=True)
SupplierEmailListSchema = list[SupplierEmailResponseSchema]

# Активность/статистика по поставщикам
class SupplierStatsResponseSchema(BaseModel):
    total: int
    with_email: int
    with_phone: int
    unique_domains: int
    model_config = ConfigDict(from_attributes=True)