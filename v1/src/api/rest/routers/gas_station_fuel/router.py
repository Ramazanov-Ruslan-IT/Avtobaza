from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.gas_station_fuel.dependencies import get_gas_station_fuel_service, AbsGasStationFuelService
from v1.src.app.dto.gas_station_fuel import GasStationFuelDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.gas_station_fuel.schemas import (
    GasStationFuelCreateSchema, GasStationFuelGetSchema, GasStationFuelUpdateSchema, GasStationFuelDeleteSchema,
    GasStationFuelResponseSchema1, GasStationFuelResponseSchema2, GasStationFuelResponseSchema3, GasStationFuelResponseSchema4
)

router = APIRouter(prefix="/gas_station_fuel", tags=["GasStationFuel"])

@api_post(router, "", GasStationFuelResponseSchema1, summary="Создать топливо на АЗС")
async def create_gas_station_fuel(
    gas_station_fuel: GasStationFuelCreateSchema = Body(...),
    gas_station_fuel_service: AbsGasStationFuelService = Depends(get_gas_station_fuel_service),
):
    try:
        result = await gas_station_fuel_service.create_gas_station_fuel(pydantic_to_dto(GasStationFuelDTO, gas_station_fuel))
        if not result:
            raise_404(data={"errors": "GasStationFuel not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", GasStationFuelResponseSchema2, summary="Получить топливо на АЗС")
async def get_gas_station_fuel(
    gas_station_fuel: GasStationFuelGetSchema = Query(...),
    gas_station_fuel_service: AbsGasStationFuelService = Depends(get_gas_station_fuel_service),
):
    try:
        result = await gas_station_fuel_service.get_gas_station_fuel(pydantic_to_dto(GasStationFuelDTO, gas_station_fuel))
        if not result:
            raise_404(data={"errors": "GasStationFuel not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", GasStationFuelResponseSchema3, summary="Обновить топливо на АЗС")
async def update_gas_station_fuel(
    gas_station_fuel: GasStationFuelUpdateSchema = Body(...),
    gas_station_fuel_service: AbsGasStationFuelService = Depends(get_gas_station_fuel_service),
):
    try:
        result = await gas_station_fuel_service.update_gas_station_fuel(pydantic_to_dto(GasStationFuelDTO, gas_station_fuel))
        if not result:
            raise_404(data={"errors": "GasStationFuel not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", GasStationFuelResponseSchema4, summary="Удалить топливо на АЗС")
async def delete_gas_station_fuel(
    gas_station_fuel: GasStationFuelDeleteSchema = Body(...),
    gas_station_fuel_service: AbsGasStationFuelService = Depends(get_gas_station_fuel_service),
):
    try:
        result = await gas_station_fuel_service.delete_gas_station_fuel(pydantic_to_dto(GasStationFuelDTO, gas_station_fuel))
        if not result:
            raise_404(data={"errors": "GasStationFuel not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
