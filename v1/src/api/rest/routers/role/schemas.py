from pydantic import BaseModel, ConfigDict

class RoleCreateSchema(BaseModel):
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)

class RoleGetSchema(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)

class RoleUpdateSchema(BaseModel):
    id: int
    name: str | None = None
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)

class RoleDeleteSchema(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)

class RoleResponseSchema1(BaseModel):
    id: int
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)

class RoleResponseSchema2(RoleResponseSchema1): pass
class RoleResponseSchema3(RoleResponseSchema1): pass
class RoleResponseSchema4(RoleResponseSchema1): pass
