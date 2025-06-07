from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.user.dependencies import get_user_service, AbsUserService
from v1.src.app.dto.user import UserDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.user.schemas import (
    UserCreateSchema, UserGetSchema, UserUpdateSchema, UserDeleteSchema,
    UserResponseSchema1, UserResponseSchema2, UserResponseSchema3, UserResponseSchema4
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
