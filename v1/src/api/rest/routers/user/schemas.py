from pydantic import BaseModel, ConfigDict

class UserCreateSchema(BaseModel):
    email: str
    full_name: str
    password_hash: str
    role_id: int

    model_config = ConfigDict(from_attributes=True)

class UserGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class UserUpdateSchema(BaseModel):
    id: str
    email: str | None = None
    full_name: str | None = None
    password_hash: str | None = None
    role_id: int | None = None

    model_config = ConfigDict(from_attributes=True)

class UserDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class UserResponseSchema1(BaseModel):
    id: str
    email: str
    full_name: str
    password_hash: str
    role_id: int

    model_config = ConfigDict(from_attributes=True)

class UserResponseSchema2(UserResponseSchema1): pass
class UserResponseSchema3(UserResponseSchema1): pass
class UserResponseSchema4(UserResponseSchema1): pass

class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str

class BatchUpdateRoleSchema(BaseModel):
    user_ids: list[str]
    new_role_id: int
