from fastapi import Depends, Body, APIRouter, Query
from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.autobase.dependencies import get_autobase_service, AbsAutobaseService
from v1.src.app.dto.autobase import AutobaseDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.autobase.schemas import (
    AutobaseCreateSchema, AutobaseGetSchema, AutobaseUpdateSchema, AutobaseDeleteSchema,
    AutobaseResponseSchema1, AutobaseResponseSchema2, AutobaseResponseSchema3, AutobaseResponseSchema4,
    AutobaseListSchema, AutobaseSearchSchema, AutobaseSearchListSchema, AutobaseStatsListSchema
)

router = APIRouter(prefix="/autobase", tags=["Autobase"])

# --- CRUD ---

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

# --- Дополнительные endpoint-ы ---

@api_get(router, "/list", AutobaseListSchema, summary="Список автобаз")
async def list_autobases(
    skip: int = Query(0),
    limit: int = Query(20),
):
    # Заглушка: просто тестовые объекты
    return [
        AutobaseResponseSchema1(
            id=str(i),
            name=f"База №{i}",
            address=f"Город {i}, ул. Примерная, д.{i+1}",
            latitude=55.7 + i * 0.1,
            longitude=37.5 + i * 0.1,
        ) for i in range(skip, skip + limit)
    ]

@api_get(router, "/search", AutobaseSearchListSchema, summary="Поиск автобаз")
async def search_autobases(
    name: str = Query(None),
    address: str = Query(None),
    lat_from: float = Query(None),
    lat_to: float = Query(None),
    lon_from: float = Query(None),
    lon_to: float = Query(None),
):
    # Заглушка — обычно фильтрация идёт по ORM
    return [
        AutobaseResponseSchema1(
            id="base_42",
            name=name or "СпецБаза",
            address=address or "Москва, Автозаводская 1",
            latitude=lat_from or 55.1,
            longitude=lon_from or 37.1,
        )
    ]

@api_get(router, "/stats", AutobaseStatsListSchema, summary="Статистика по автобазам")
async def autobase_stats():
    return [
        {"id": "1", "name": "Автобаза №1", "vehicles_count": 24, "storage_fuel_litres": 18200, "open_repairs": 2},
        {"id": "2", "name": "Грузовой двор", "vehicles_count": 16, "storage_fuel_litres": 11200, "open_repairs": 0},
        {"id": "3", "name": "База ВДНХ", "vehicles_count": 32, "storage_fuel_litres": 25400, "open_repairs": 5},
    ]
