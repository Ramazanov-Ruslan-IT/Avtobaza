from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.vehicle.dependencies import get_vehicle_service, AbsVehicleService
from v1.src.app.dto.vehicle import VehicleDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.vehicle.schemas import (
    VehicleCreateSchema, VehicleGetSchema, VehicleUpdateSchema, VehicleDeleteSchema,
    VehicleResponseSchema1, VehicleResponseSchema2, VehicleResponseSchema3, VehicleResponseSchema4
)

router = APIRouter(prefix="/vehicle", tags=["Vehicle"])

@api_post(router, "", VehicleResponseSchema1, summary="Создать транспортное средство")
async def create_vehicle(
    vehicle: VehicleCreateSchema = Body(...),
    vehicle_service: AbsVehicleService = Depends(get_vehicle_service),
):
    try:
        result = await vehicle_service.create_vehicle(pydantic_to_dto(VehicleDTO, vehicle))
        if not result:
            raise_404(data={"errors": "Vehicle not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", VehicleResponseSchema2, summary="Получить транспортное средство")
async def get_vehicle(
    vehicle: VehicleGetSchema = Query(...),
    vehicle_service: AbsVehicleService = Depends(get_vehicle_service),
):
    try:
        result = await vehicle_service.get_vehicle(pydantic_to_dto(VehicleDTO, vehicle))
        if not result:
            raise_404(data={"errors": "Vehicle not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", VehicleResponseSchema3, summary="Обновить транспортное средство")
async def update_vehicle(
    vehicle: VehicleUpdateSchema = Body(...),
    vehicle_service: AbsVehicleService = Depends(get_vehicle_service),
):
    try:
        result = await vehicle_service.update_vehicle(pydantic_to_dto(VehicleDTO, vehicle))
        if not result:
            raise_404(data={"errors": "Vehicle not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", VehicleResponseSchema4, summary="Удалить транспортное средство")
async def delete_vehicle(
    vehicle: VehicleDeleteSchema = Body(...),
    vehicle_service: AbsVehicleService = Depends(get_vehicle_service),
):
    try:
        result = await vehicle_service.delete_vehicle(pydantic_to_dto(VehicleDTO, vehicle))
        if not result:
            raise_404(data={"errors": "Vehicle not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
