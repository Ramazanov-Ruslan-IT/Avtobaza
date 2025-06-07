from fastapi import Depends, Body, APIRouter, Query, Path, status

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.user.dependencies import get_user_service, AbsUserService
from v1.src.app.dto.user import UserDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.user.schemas import (
    UserCreateSchema, UserGetSchema, UserUpdateSchema, UserDeleteSchema,
    UserResponseSchema1, UserResponseSchema2, UserResponseSchema3, UserResponseSchema4, ChangePasswordSchema,
    BatchUpdateRoleSchema
)

router = APIRouter(prefix="/user", tags=["User"])


@api_post(router, "", UserResponseSchema1, summary="Создать пользователя")
async def create_user(
    user: UserCreateSchema = Body(...),
    user_service: AbsUserService = Depends(get_user_service),
):
    try:
        result = await user_service.create_user(pydantic_to_dto(UserDTO, user))
        if not result:
            raise_404(data={"errors": "User not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})


@api_get(router, "", UserResponseSchema2, summary="Получить пользователя")
async def get_user(
    user: UserGetSchema = Query(...),
    user_service: AbsUserService = Depends(get_user_service),
):
    try:
        result = await user_service.get_user(pydantic_to_dto(UserDTO, user))
        if not result:
            raise_404(data={"errors": "User not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})


@api_put(router, "", UserResponseSchema3, summary="Обновить пользователя")
async def update_user(
    user: UserUpdateSchema = Body(...),
    user_service: AbsUserService = Depends(get_user_service),
):
    try:
        result = await user_service.update_user(pydantic_to_dto(UserDTO, user))
        if not result:
            raise_404(data={"errors": "User not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})


@api_delete(router, "", UserResponseSchema4, summary="Удалить пользователя")
async def delete_user(
    user: UserDeleteSchema = Body(...),
    user_service: AbsUserService = Depends(get_user_service),
):
    try:
        result = await user_service.delete_user(pydantic_to_dto(UserDTO, user))
        if not result:
            raise_404(data={"errors": "User not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})


@api_get(router, "/list", list[UserResponseSchema1], summary="Получить список всех пользователей")
async def list_users(
    skip: int = Query(0, description="Сколько пропустить"),
    limit: int = Query(10, description="Сколько вернуть"),
    role_id: int | None = Query(None, description="Фильтр по роли"),
    user_service: AbsUserService = Depends(get_user_service),
):
    return [
        UserResponseSchema1(
            id=str(i),
            email=f"user{i}@test.com",
            full_name=f"User {i}",
            password_hash="***",
            role_id=role_id or 1
        )
        for i in range(skip, skip + limit)
    ]


@api_get(router, "/profile/{user_id}", UserResponseSchema1, summary="Получить профиль пользователя по ID")
async def get_user_profile(
    user_id: str = Path(..., description="ID пользователя"),
    user_service: AbsUserService = Depends(get_user_service),
):
    return UserResponseSchema1(
        id=user_id,
        email=f"profile_{user_id}@test.com",
        full_name=f"Profile User {user_id}",
        password_hash="***",
        role_id=2
    )


@api_post(router, "/{user_id}/change-password", dict, summary="Сменить пароль пользователя")
async def change_user_password(
    user_id: str = Path(..., description="ID пользователя"),
    body: ChangePasswordSchema = Body(...),
    user_service: AbsUserService = Depends(get_user_service),
):
    return None


@api_put(router, "/batch-update-role", list[UserResponseSchema1], summary="Массовое обновление ролей пользователей")
async def batch_update_user_role(
    data: BatchUpdateRoleSchema = Body(...),
    user_service: AbsUserService = Depends(get_user_service),
):
    return [
        UserResponseSchema1(
            id=uid,
            email=f"user{uid}@test.com",
            full_name=f"User {uid}",
            password_hash="***",
            role_id=data.new_role_id
        ) for uid in data.user_ids
    ]


@api_get(router, "/search", list[UserResponseSchema1], summary="Поиск пользователей по email/ФИО")
async def search_users(
    query: str = Query(..., description="Поисковый запрос (email или ФИО)"),
    user_service: AbsUserService = Depends(get_user_service),
):
    return [
        UserResponseSchema1(
            id="111",
            email=f"{query}_1@test.com",
            full_name=f"{query} Ivanov",
            password_hash="***",
            role_id=1
        ),
        UserResponseSchema1(
            id="112",
            email=f"{query}_2@test.com",
            full_name=f"{query} Petrov",
            password_hash="***",
            role_id=2
        )
    ]


@api_post(router, "/login", UserResponseSchema1, summary="Авторизация пользователя")
async def login_user(
    email: str = Body(...),
    password: str = Body(...),
    user_service: AbsUserService = Depends(get_user_service),
):
    if password == "test":
        return UserResponseSchema1(
            id="login_ok",
            email=email,
            full_name="Test User",
            password_hash="***",
            role_id=1
        )
    raise_404(data={"errors": "Invalid credentials"})
