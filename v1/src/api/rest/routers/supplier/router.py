from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.supplier.dependencies import get_supplier_service, AbsSupplierService
from v1.src.app.dto.supplier import SupplierDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.supplier.schemas import (
    SupplierCreateSchema, SupplierGetSchema, SupplierUpdateSchema, SupplierDeleteSchema,
    SupplierResponseSchema1, SupplierResponseSchema2, SupplierResponseSchema3, SupplierResponseSchema4
)

router = APIRouter(prefix="/supplier", tags=["Supplier"])

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
