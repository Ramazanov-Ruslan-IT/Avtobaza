from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.gas_station.dependencies import get_gas_station_service, AbsGasStationService
from v1.src.app.dto.gas_station import GasStationDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.gas_station.schemas import (
    GasStationCreateSchema, GasStationGetSchema, GasStationUpdateSchema, GasStationDeleteSchema,
    GasStationResponseSchema1, GasStationResponseSchema2, GasStationResponseSchema3, GasStationResponseSchema4
)

router = APIRouter(prefix="/gas_station", tags=["GasStation"])

@api_post(router, "", GasStationResponseSchema1, summary="Создать АЗС")
async def create_gas_station(
    gas_station: GasStationCreateSchema = Body(...),
    gas_station_service: AbsGasStationService = Depends(get_gas_station_service),
):
    try:
        result = await gas_station_service.create_gas_station(pydantic_to_dto(GasStationDTO, gas_station))
        if not result:
            raise_404(data={"errors": "GasStation not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", GasStationResponseSchema2, summary="Получить АЗС")
async def get_gas_station(
    gas_station: GasStationGetSchema = Query(...),
    gas_station_service: AbsGasStationService = Depends(get_gas_station_service),
):
    try:
        result = await gas_station_service.get_gas_station(pydantic_to_dto(GasStationDTO, gas_station))
        if not result:
            raise_404(data={"errors": "GasStation not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", GasStationResponseSchema3, summary="Обновить АЗС")
async def update_gas_station(
    gas_station: GasStationUpdateSchema = Body(...),
    gas_station_service: AbsGasStationService = Depends(get_gas_station_service),
):
    try:
        result = await gas_station_service.update_gas_station(pydantic_to_dto(GasStationDTO, gas_station))
        if not result:
            raise_404(data={"errors": "GasStation not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", GasStationResponseSchema4, summary="Удалить АЗС")
async def delete_gas_station(
    gas_station: GasStationDeleteSchema = Body(...),
    gas_station_service: AbsGasStationService = Depends(get_gas_station_service),
):
    try:
        result = await gas_station_service.delete_gas_station(pydantic_to_dto(GasStationDTO, gas_station))
        if not result:
            raise_404(data={"errors": "GasStation not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
