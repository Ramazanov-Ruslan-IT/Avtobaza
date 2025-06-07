from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.autobase.dependencies import get_autobase_service, AbsAutobaseService
from v1.src.app.dto.autobase import AutobaseDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.autobase.schemas import (
    AutobaseCreateSchema, AutobaseGetSchema, AutobaseUpdateSchema, AutobaseDeleteSchema,
    AutobaseResponseSchema1, AutobaseResponseSchema2, AutobaseResponseSchema3, AutobaseResponseSchema4
)

router = APIRouter(prefix="/autobase", tags=["Autobase"])

@api_post(router, "", AutobaseResponseSchema1, summary="Создать автобазу")
async def create_autobase(
    autobase: AutobaseCreateSchema = Body(...),
    autobase_service: AbsAutobaseService = Depends(get_autobase_service),
):
    try:
        result = await autobase_service.create_autobase(pydantic_to_dto(AutobaseDTO, autobase))
        if not result:
            raise_404(data={"errors": "Autobase not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", AutobaseResponseSchema2, summary="Получить автобазу")
async def get_autobase(
    autobase: AutobaseGetSchema = Query(...),
    autobase_service: AbsAutobaseService = Depends(get_autobase_service),
):
    try:
        result = await autobase_service.get_autobase(pydantic_to_dto(AutobaseDTO, autobase))
        if not result:
            raise_404(data={"errors": "Autobase not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", AutobaseResponseSchema3, summary="Обновить автобазу")
async def update_autobase(
    autobase: AutobaseUpdateSchema = Body(...),
    autobase_service: AbsAutobaseService = Depends(get_autobase_service),
):
    try:
        result = await autobase_service.update_autobase(pydantic_to_dto(AutobaseDTO, autobase))
        if not result:
            raise_404(data={"errors": "Autobase not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", AutobaseResponseSchema4, summary="Удалить автобазу")
async def delete_autobase(
    autobase: AutobaseDeleteSchema = Body(...),
    autobase_service: AbsAutobaseService = Depends(get_autobase_service),
):
    try:
        result = await autobase_service.delete_autobase(pydantic_to_dto(AutobaseDTO, autobase))
        if not result:
            raise_404(data={"errors": "Autobase not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
