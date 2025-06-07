from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.role.dependencies import get_role_service, AbsRoleService
from v1.src.app.dto.role import RoleDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.role.schemas import (
    RoleCreateSchema, RoleGetSchema, RoleUpdateSchema, RoleDeleteSchema,
    RoleResponseSchema1, RoleResponseSchema2, RoleResponseSchema3, RoleResponseSchema4
)

router = APIRouter(prefix="/role", tags=["Role"])

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
