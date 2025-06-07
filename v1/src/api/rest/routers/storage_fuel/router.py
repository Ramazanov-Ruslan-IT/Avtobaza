from datetime import datetime

from fastapi import Depends, Body, APIRouter, Query, Path

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.storage_fuel.dependencies import get_storage_fuel_service, AbsStorageFuelService
from v1.src.app.dto.storage_fuel import StorageFuelDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.storage_fuel.schemas import (
    StorageFuelCreateSchema, StorageFuelGetSchema, StorageFuelUpdateSchema, StorageFuelDeleteSchema,
    StorageFuelResponseSchema1, StorageFuelResponseSchema2, StorageFuelResponseSchema3, StorageFuelResponseSchema4,
    StorageFuelListSchema, StorageFuelSearchSchema, StorageFuelSearchListSchema,
    StorageFuelStatsSchema, StorageFuelStatsListSchema
)

router = APIRouter(prefix="/storage_fuel", tags=["StorageFuel"])

# --- CRUD ---

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

# --- Дополнительные endpoint-ы ---

@api_get(router, "/list", StorageFuelListSchema, summary="Список остатков топлива по складам")
async def list_storage_fuel(
    skip: int = Query(0, description="Сколько пропустить"),
    limit: int = Query(10, description="Сколько вернуть"),
):
    # Заглушка: N остатков для фронта
    return [
        StorageFuelResponseSchema1(
            id=str(i),
            autobase_id=f"autobase{i%3}",
            fuel_type_id=(i % 5) + 1,
            litres=1000.0 - 50.0 * i,
            last_updated=datetime.now()
        ) for i in range(skip, skip + limit)
    ]

@api_get(router, "/search", StorageFuelSearchListSchema, summary="Поиск остатков по складу/топливу")
async def search_storage_fuel(
    autobase_id: str = Query(None),
    fuel_type_id: int = Query(None),
):
    # Заглушка: фильтрация по autobase_id и fuel_type_id (фейковые данные)
    return [
        StorageFuelResponseSchema1(
            id="1",
            autobase_id=autobase_id or "autobase1",
            fuel_type_id=fuel_type_id or 2,
            litres=500.0,
            last_updated=datetime.now()
        )
    ]

@api_get(router, "/stats", StorageFuelStatsListSchema, summary="Статистика остатков по складам")
async def storage_fuel_stats():
    return [
        StorageFuelStatsSchema(
            autobase_id=f"autobase{i}",
            total_litres=10_000 - 1000 * i,
            last_update=datetime.now()
        ) for i in range(3)
    ]
