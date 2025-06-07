from fastapi import Depends, Body, APIRouter, Query, Path

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.role.dependencies import get_role_service, AbsRoleService
from v1.src.app.dto.role import RoleDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.role.schemas import (
    RoleCreateSchema, RoleGetSchema, RoleUpdateSchema, RoleDeleteSchema,
    RoleResponseSchema1, RoleResponseSchema2, RoleResponseSchema3, RoleResponseSchema4,
    RoleListSchema, RoleNameCheckSchema, RoleNameCheckResponseSchema,
    RoleBatchCreateSchema, RoleUsersListSchema, RoleUsersResponseSchema
)

router = APIRouter(prefix="/role", tags=["Role"])

# --- CRUD ---

@api_post(router, "", RoleResponseSchema1, summary="Создать роль")
async def create_role(
    role: RoleCreateSchema = Body(...),
    role_service: AbsRoleService = Depends(get_role_service),
):
    try:
        result = await role_service.create_role(pydantic_to_dto(RoleDTO, role))
        if not result:
            raise_404(data={"errors": "Role not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", RoleResponseSchema2, summary="Получить роль")
async def get_role(
    role: RoleGetSchema = Query(...),
    role_service: AbsRoleService = Depends(get_role_service),
):
    try:
        result = await role_service.get_role(pydantic_to_dto(RoleDTO, role))
        if not result:
            raise_404(data={"errors": "Role not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", RoleResponseSchema3, summary="Обновить роль")
async def update_role(
    role: RoleUpdateSchema = Body(...),
    role_service: AbsRoleService = Depends(get_role_service),
):
    try:
        result = await role_service.update_role(pydantic_to_dto(RoleDTO, role))
        if not result:
            raise_404(data={"errors": "Role not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", RoleResponseSchema4, summary="Удалить роль")
async def delete_role(
    role: RoleDeleteSchema = Body(...),
    role_service: AbsRoleService = Depends(get_role_service),
):
    try:
        result = await role_service.delete_role(pydantic_to_dto(RoleDTO, role))
        if not result:
            raise_404(data={"errors": "Role not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

# --- Дополнительные endpoint-ы ---

@api_get(router, "/list", RoleListSchema, summary="Список всех ролей")
async def list_roles():
    # Заглушка: 3 фейковые роли
    return [
        RoleResponseSchema1(id=1, name="admin", description="Администратор"),
        RoleResponseSchema1(id=2, name="manager", description="Менеджер"),
        RoleResponseSchema1(id=3, name="driver", description="Водитель"),
    ]

@api_post(router, "/batch", RoleListSchema, summary="Массовое создание ролей")
async def batch_create_roles(
    data: RoleBatchCreateSchema = Body(...),
):
    return [
        RoleResponseSchema1(id=idx+100, name=role.name, description=role.description)
        for idx, role in enumerate(data.roles)
    ]

@api_get(router, "/check-name", RoleNameCheckResponseSchema, summary="Проверить уникальность имени роли")
async def check_role_name(
    data: RoleNameCheckSchema = Depends(),
):
    # Заглушка: любое имя, кроме "admin", уникально
    return RoleNameCheckResponseSchema(is_unique=(data.name != "admin"))

@api_get(router, "/{role_id}/users", RoleUsersListSchema, summary="Список пользователей с ролью")
async def get_role_users(
    role_id: int = Path(...),
):
    # Заглушка: всегда 2 пользователя
    return [
        RoleUsersResponseSchema(user_id="u1001", email="ivan@test.ru", full_name="Иван Иванов"),
        RoleUsersResponseSchema(user_id="u1002", email="petr@test.ru", full_name="Пётр Петров"),
    ]
