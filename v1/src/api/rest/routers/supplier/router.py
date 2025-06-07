from fastapi import Depends, Body, APIRouter, Query, Path

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.supplier.dependencies import get_supplier_service, AbsSupplierService
from v1.src.app.dto.supplier import SupplierDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.supplier.schemas import (
    SupplierCreateSchema, SupplierGetSchema, SupplierUpdateSchema, SupplierDeleteSchema,
    SupplierResponseSchema1, SupplierResponseSchema2, SupplierResponseSchema3, SupplierResponseSchema4,
    SupplierListSchema, SupplierBatchOperationSchema, SupplierBatchDeleteSchema,
    SupplierSearchListSchema, SupplierEmailListSchema, SupplierStatsResponseSchema
)

router = APIRouter(prefix="/supplier", tags=["Supplier"])

# --- CRUD ---

@api_post(router, "", SupplierResponseSchema1, summary="Создать поставщика")
async def create_supplier(
    supplier: SupplierCreateSchema = Body(...),
    supplier_service: AbsSupplierService = Depends(get_supplier_service),
):
    try:
        result = await supplier_service.create_supplier(pydantic_to_dto(SupplierDTO, supplier))
        if not result:
            raise_404(data={"errors": "Supplier not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", SupplierResponseSchema2, summary="Получить поставщика")
async def get_supplier(
    supplier: SupplierGetSchema = Query(...),
    supplier_service: AbsSupplierService = Depends(get_supplier_service),
):
    try:
        result = await supplier_service.get_supplier(pydantic_to_dto(SupplierDTO, supplier))
        if not result:
            raise_404(data={"errors": "Supplier not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", SupplierResponseSchema3, summary="Обновить поставщика")
async def update_supplier(
    supplier: SupplierUpdateSchema = Body(...),
    supplier_service: AbsSupplierService = Depends(get_supplier_service),
):
    try:
        result = await supplier_service.update_supplier(pydantic_to_dto(SupplierDTO, supplier))
        if not result:
            raise_404(data={"errors": "Supplier not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", SupplierResponseSchema4, summary="Удалить поставщика")
async def delete_supplier(
    supplier: SupplierDeleteSchema = Body(...),
    supplier_service: AbsSupplierService = Depends(get_supplier_service),
):
    try:
        result = await supplier_service.delete_supplier(pydantic_to_dto(SupplierDTO, supplier))
        if not result:
            raise_404(data={"errors": "Supplier not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

# --- Дополнительные endpoint-ы ---

@api_get(router, "/list", SupplierListSchema, summary="Список всех поставщиков")
async def list_suppliers(
    skip: int = Query(0, description="Сколько пропустить"),
    limit: int = Query(10, description="Сколько вернуть"),
):
    # Заглушка: тестовые поставщики
    return [
        SupplierResponseSchema1(
            id=f"{i}",
            name=f"Поставщик {i}",
            contact_email=f"supplier{i}@mail.com",
            phone=f"+7000000{i:03d}",
            address=f"Город {i}"
        ) for i in range(skip, skip + limit)
    ]

@api_post(router, "/batch", SupplierListSchema, summary="Массовое создание поставщиков")
async def batch_create_suppliers(
    data: SupplierBatchOperationSchema = Body(...),
):
    # Заглушка: все новые поставщики с id от 1000+
    return [
        SupplierResponseSchema1(
            id=str(1000 + idx),
            name=s.name,
            contact_email=s.contact_email,
            phone=s.phone,
            address=s.address
        ) for idx, s in enumerate(data.suppliers)
    ]

@api_delete(router, "/batch", SupplierListSchema, summary="Массовое удаление поставщиков")
async def batch_delete_suppliers(
    data: SupplierBatchDeleteSchema = Body(...),
):
    # Заглушка: возвращаем удалённые id
    return [
        SupplierResponseSchema1(
            id=uid,
            name=f"DELETED_{uid}",
            contact_email="",
            phone="",
            address=""
        ) for uid in data.ids
    ]

@api_get(router, "/search", SupplierSearchListSchema, summary="Поиск поставщиков по имени/email")
async def search_suppliers(
    query: str = Query(..., description="Часть имени или email"),
):
    # Заглушка: пара совпадений
    return [
        SupplierResponseSchema1(
            id="s101",
            name=f"{query} Company",
            contact_email=f"{query}@mail.com",
            phone="+71234567890",
            address="Тестовый адрес"
        ),
        SupplierResponseSchema1(
            id="s102",
            name=f"{query} Group",
            contact_email=f"info@{query}.org",
            phone="+79876543210",
            address="Другое местоположение"
        ),
    ]

@api_get(router, "/emails", SupplierEmailListSchema, summary="Все email поставщиков")
async def get_supplier_emails():
    # Заглушка: просто email'ы
    return [
        {"contact_email": "test1@mail.com"},
        {"contact_email": "test2@corp.ru"},
        {"contact_email": "info@company.org"},
    ]

@api_get(router, "/stats", SupplierStatsResponseSchema, summary="Статистика по поставщикам")
async def get_supplier_stats():
    return SupplierStatsResponseSchema(
        total=127,
        with_email=125,
        with_phone=120,
        unique_domains=16
    )
