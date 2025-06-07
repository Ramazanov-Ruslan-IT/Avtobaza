from datetime import datetime
from pydantic import BaseModel, ConfigDict

class DocumentCreateSchema(BaseModel):
    vehicle_id: str
    doc_type: str
    file_url: str
    uploaded_by: str
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DocumentGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class DocumentUpdateSchema(BaseModel):
    id: str
    vehicle_id: str | None = None
    doc_type: str | None = None
    file_url: str | None = None
    uploaded_by: str | None = None
    uploaded_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class DocumentDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class DocumentResponseSchema1(BaseModel):
    id: str
    vehicle_id: str
    doc_type: str
    file_url: str
    uploaded_by: str
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DocumentResponseSchema2(DocumentResponseSchema1): pass
class DocumentResponseSchema3(DocumentResponseSchema1): pass
class DocumentResponseSchema4(DocumentResponseSchema1): pass
