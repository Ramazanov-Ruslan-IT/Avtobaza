from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.fuel_type.dependencies import get_fuel_type_service, AbsFuelTypeService
from v1.src.app.dto.fuel_type import FuelTypeDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.fuel_type.schemas import (
    FuelTypeCreateSchema, FuelTypeGetSchema, FuelTypeUpdateSchema, FuelTypeDeleteSchema,
    FuelTypeResponseSchema1, FuelTypeResponseSchema2, FuelTypeResponseSchema3, FuelTypeResponseSchema4
)

router = APIRouter(prefix="/fuel_type", tags=["FuelType"])

@api_post(router, "", FuelTypeResponseSchema1, summary="Создать тип топлива")
async def create_fuel_type(
    fuel_type: FuelTypeCreateSchema = Body(...),
    fuel_type_service: AbsFuelTypeService = Depends(get_fuel_type_service),
):
    try:
        result = await fuel_type_service.create_fuel_type(pydantic_to_dto(FuelTypeDTO, fuel_type))
        if not result:
            raise_404(data={"errors": "FuelType not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", FuelTypeResponseSchema2, summary="Получить тип топлива")
async def get_fuel_type(
    fuel_type: FuelTypeGetSchema = Query(...),
    fuel_type_service: AbsFuelTypeService = Depends(get_fuel_type_service),
):
    try:
        result = await fuel_type_service.get_fuel_type(pydantic_to_dto(FuelTypeDTO, fuel_type))
        if not result:
            raise_404(data={"errors": "FuelType not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", FuelTypeResponseSchema3, summary="Обновить тип топлива")
async def update_fuel_type(
    fuel_type: FuelTypeUpdateSchema = Body(...),
    fuel_type_service: AbsFuelTypeService = Depends(get_fuel_type_service),
):
    try:
        result = await fuel_type_service.update_fuel_type(pydantic_to_dto(FuelTypeDTO, fuel_type))
        if not result:
            raise_404(data={"errors": "FuelType not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", FuelTypeResponseSchema4, summary="Удалить тип топлива")
async def delete_fuel_type(
    fuel_type: FuelTypeDeleteSchema = Body(...),
    fuel_type_service: AbsFuelTypeService = Depends(get_fuel_type_service),
):
    try:
        result = await fuel_type_service.delete_fuel_type(pydantic_to_dto(FuelTypeDTO, fuel_type))
        if not result:
            raise_404(data={"errors": "FuelType not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
