from datetime import datetime
from pydantic import BaseModel, ConfigDict

class MlSuggestionCreateSchema(BaseModel):
    suggestion_type: str
    target_entity: str
    entity_id: str
    message: str
    created_at: datetime
    resolved: bool

    model_config = ConfigDict(from_attributes=True)

class MlSuggestionGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class MlSuggestionUpdateSchema(BaseModel):
    id: str
    suggestion_type: str | None = None
    target_entity: str | None = None
    entity_id: str | None = None
    message: str | None = None
    created_at: datetime | None = None
    resolved: bool | None = None

    model_config = ConfigDict(from_attributes=True)

class MlSuggestionDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class MlSuggestionResponseSchema1(BaseModel):
    id: str
    suggestion_type: str
    target_entity: str
    entity_id: str
    message: str
    created_at: datetime
    resolved: bool

    model_config = ConfigDict(from_attributes=True)

class MlSuggestionResponseSchema2(MlSuggestionResponseSchema1): pass
class MlSuggestionResponseSchema3(MlSuggestionResponseSchema1): pass
class MlSuggestionResponseSchema4(MlSuggestionResponseSchema1): pass
