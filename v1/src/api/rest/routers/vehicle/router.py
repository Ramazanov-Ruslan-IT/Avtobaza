from fastapi import Depends, Body, APIRouter, Query, Path
from typing import List, Optional

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.vehicle.dependencies import get_vehicle_service, AbsVehicleService
from v1.src.app.dto.vehicle import VehicleDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.vehicle.schemas import (
    VehicleCreateSchema, VehicleGetSchema, VehicleUpdateSchema, VehicleDeleteSchema,
    VehicleResponseSchema1, VehicleResponseSchema2, VehicleResponseSchema3, VehicleResponseSchema4,
    VehicleListSchema, VehicleHistoryEventSchema, AssignDriverRequestSchema, AssignDriverResponseSchema,
    VehicleMileageResponseSchema, FleetAnalyticsResponseSchema, VehicleHistoryResponseSchema
)

router = APIRouter(prefix="/vehicle", tags=["Vehicle"])

# --- CRUD ---

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

# --- Дополнительные endpoint-ы с новыми схемами ---

@api_get(router, "/list", VehicleListSchema, summary="Список всех транспортных средств")
async def list_vehicles(
    skip: int = Query(0, description="Сколько пропустить"),
    limit: int = Query(10, description="Сколько вернуть"),
    status: Optional[str] = Query(None),
    autobase_id: Optional[str] = Query(None),
):
    return [
        VehicleResponseSchema1(
            id=f"{i}",
            license_plate=f"ТЕСТ{i}РУС",
            brand="Lada",
            model=f"Vesta{i}",
            body_type="sedan",
            vin=f"VIN{i}123456789",
            fuel_type_id=1,
            autobase_id=autobase_id or "autobase1",
            status=status or "active",
            mileage=10000 + i * 100
        )
        for i in range(skip, skip + limit)
    ]

@api_get(router, "/search", VehicleListSchema, summary="Поиск ТС по госномеру или VIN")
async def search_vehicle(
    query: str = Query(..., description="Госномер или VIN"),
):
    return [
        VehicleResponseSchema1(
            id="42",
            license_plate=query,
            brand="Toyota",
            model="Camry",
            body_type="sedan",
            vin=query,
            fuel_type_id=2,
            autobase_id="autobase2",
            status="active",
            mileage=123456
        )
    ]

@api_get(router, "/history/{vehicle_id}", VehicleHistoryResponseSchema, summary="История эксплуатации по ID машины")
async def get_vehicle_history(
    vehicle_id: str = Path(...),
):
    return [
        VehicleHistoryEventSchema(event=f"2024-01-12: ТО-1 проведено"),
        VehicleHistoryEventSchema(event=f"2024-02-03: Замена масла"),
        VehicleHistoryEventSchema(event=f"2024-03-21: Заправка на АЗС"),
        VehicleHistoryEventSchema(event=f"2024-04-10: Заявка на ремонт"),
        VehicleHistoryEventSchema(event=f"2024-05-05: Маршрут до Новосибирска")
    ]

@api_post(router, "/assign-driver/{vehicle_id}", AssignDriverResponseSchema, summary="Назначить водителя на ТС")
async def assign_driver(
    vehicle_id: str = Path(...),
    body: AssignDriverRequestSchema = Body(...),
):
    return AssignDriverResponseSchema(success=True, message=f"Водитель {body.driver_id} назначен на {vehicle_id}")

@api_get(router, "/mileage/{vehicle_id}", VehicleMileageResponseSchema, summary="Текущий пробег по ID машины")
async def get_vehicle_mileage(
    vehicle_id: str = Path(...),
):
    return VehicleMileageResponseSchema(vehicle_id=vehicle_id, mileage=150_000.0)

@api_get(router, "/analytics", FleetAnalyticsResponseSchema, summary="Аналитика по автопарку")
async def fleet_analytics():
    return FleetAnalyticsResponseSchema(
        avg_mileage=125_000,
        max_mileage=440_000,
        total_fuel_cost=4_200_000,
        vehicles_in_service=42,
        vehicles_under_repair=4
    )
