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

from pydantic import BaseModel, ConfigDict

# CRUD-схемы — у тебя уже есть выше

# Для списка всех ролей
RoleListSchema = list[RoleResponseSchema1]

# Для проверки уникальности имени роли
class RoleNameCheckSchema(BaseModel):
    name: str
    model_config = ConfigDict(from_attributes=True)

class RoleNameCheckResponseSchema(BaseModel):
    is_unique: bool
    model_config = ConfigDict(from_attributes=True)

# Для массового создания ролей
class RoleBatchCreateSchema(BaseModel):
    roles: list[RoleCreateSchema]
    model_config = ConfigDict(from_attributes=True)

# Для выдачи всех пользователей с данной ролью (role_id → user list)
class RoleUsersResponseSchema(BaseModel):
    user_id: str
    email: str
    full_name: str
    model_config = ConfigDict(from_attributes=True)
RoleUsersListSchema = list[RoleUsersResponseSchema]
