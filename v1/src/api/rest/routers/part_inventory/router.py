from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.part_inventory.dependencies import get_part_inventory_service, AbsPartInventoryService
from v1.src.app.dto.part_inventory import PartInventoryDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.part_inventory.schemas import (
    PartInventoryCreateSchema, PartInventoryGetSchema, PartInventoryUpdateSchema, PartInventoryDeleteSchema,
    PartInventoryResponseSchema1, PartInventoryResponseSchema2, PartInventoryResponseSchema3, PartInventoryResponseSchema4
)

router = APIRouter(prefix="/part_inventory", tags=["PartInventory"])

@api_post(router, "", PartInventoryResponseSchema1, summary="Создать запчасть на складе")
async def create_part_inventory(
    part_inventory: PartInventoryCreateSchema = Body(...),
    part_inventory_service: AbsPartInventoryService = Depends(get_part_inventory_service),
):
    try:
        result = await part_inventory_service.create_part_inventory(pydantic_to_dto(PartInventoryDTO, part_inventory))
        if not result:
            raise_404(data={"errors": "PartInventory not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", PartInventoryResponseSchema2, summary="Получить запчасть на складе")
async def get_part_inventory(
    part_inventory: PartInventoryGetSchema = Query(...),
    part_inventory_service: AbsPartInventoryService = Depends(get_part_inventory_service),
):
    try:
        result = await part_inventory_service.get_part_inventory(pydantic_to_dto(PartInventoryDTO, part_inventory))
        if not result:
            raise_404(data={"errors": "PartInventory not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", PartInventoryResponseSchema3, summary="Обновить запчасть на складе")
async def update_part_inventory(
    part_inventory: PartInventoryUpdateSchema = Body(...),
    part_inventory_service: AbsPartInventoryService = Depends(get_part_inventory_service),
):
    try:
        result = await part_inventory_service.update_part_inventory(pydantic_to_dto(PartInventoryDTO, part_inventory))
        if not result:
            raise_404(data={"errors": "PartInventory not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", PartInventoryResponseSchema4, summary="Удалить запчасть на складе")
async def delete_part_inventory(
    part_inventory: PartInventoryDeleteSchema = Body(...),
    part_inventory_service: AbsPartInventoryService = Depends(get_part_inventory_service),
):
    try:
        result = await part_inventory_service.delete_part_inventory(pydantic_to_dto(PartInventoryDTO, part_inventory))
        if not result:
            raise_404(data={"errors": "PartInventory not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
