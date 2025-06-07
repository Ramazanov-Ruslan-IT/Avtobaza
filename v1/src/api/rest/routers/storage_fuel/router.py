from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.storage_fuel.dependencies import get_storage_fuel_service, AbsStorageFuelService
from v1.src.app.dto.storage_fuel import StorageFuelDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.storage_fuel.schemas import (
    StorageFuelCreateSchema, StorageFuelGetSchema, StorageFuelUpdateSchema, StorageFuelDeleteSchema,
    StorageFuelResponseSchema1, StorageFuelResponseSchema2, StorageFuelResponseSchema3, StorageFuelResponseSchema4
)

router = APIRouter(prefix="/storage_fuel", tags=["StorageFuel"])

@api_post(router, "", StorageFuelResponseSchema1, summary="Создать запись об остатке топлива")
async def create_storage_fuel(
    storage_fuel: StorageFuelCreateSchema = Body(...),
    storage_fuel_service: AbsStorageFuelService = Depends(get_storage_fuel_service),
):
    try:
        result = await storage_fuel_service.create_storage_fuel(pydantic_to_dto(StorageFuelDTO, storage_fuel))
        if not result:
            raise_404(data={"errors": "StorageFuel not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", StorageFuelResponseSchema2, summary="Получить запись об остатке топлива")
async def get_storage_fuel(
    storage_fuel: StorageFuelGetSchema = Query(...),
    storage_fuel_service: AbsStorageFuelService = Depends(get_storage_fuel_service),
):
    try:
        result = await storage_fuel_service.get_storage_fuel(pydantic_to_dto(StorageFuelDTO, storage_fuel))
        if not result:
            raise_404(data={"errors": "StorageFuel not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", StorageFuelResponseSchema3, summary="Обновить запись об остатке топлива")
async def update_storage_fuel(
    storage_fuel: StorageFuelUpdateSchema = Body(...),
    storage_fuel_service: AbsStorageFuelService = Depends(get_storage_fuel_service),
):
    try:
        result = await storage_fuel_service.update_storage_fuel(pydantic_to_dto(StorageFuelDTO, storage_fuel))
        if not result:
            raise_404(data={"errors": "StorageFuel not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", StorageFuelResponseSchema4, summary="Удалить запись об остатке топлива")
async def delete_storage_fuel(
    storage_fuel: StorageFuelDeleteSchema = Body(...),
    storage_fuel_service: AbsStorageFuelService = Depends(get_storage_fuel_service),
):
    try:
        result = await storage_fuel_service.delete_storage_fuel(pydantic_to_dto(StorageFuelDTO, storage_fuel))
        if not result:
            raise_404(data={"errors": "StorageFuel not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
