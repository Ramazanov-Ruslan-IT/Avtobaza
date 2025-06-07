from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.gas_station_contract.dependencies import get_gas_station_contract_service, AbsGasStationContractService
from v1.src.app.dto.gas_station_contract import GasStationContractDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.gas_station_contract.schemas import (
    GasStationContractCreateSchema, GasStationContractGetSchema, GasStationContractUpdateSchema, GasStationContractDeleteSchema,
    GasStationContractResponseSchema1, GasStationContractResponseSchema2, GasStationContractResponseSchema3, GasStationContractResponseSchema4
)

router = APIRouter(prefix="/gas_station_contract", tags=["GasStationContract"])

@api_post(router, "", GasStationContractResponseSchema1, summary="Создать договор с АЗС")
async def create_gas_station_contract(
    gas_station_contract: GasStationContractCreateSchema = Body(...),
    gas_station_contract_service: AbsGasStationContractService = Depends(get_gas_station_contract_service),
):
    try:
        result = await gas_station_contract_service.create_gas_station_contract(pydantic_to_dto(GasStationContractDTO, gas_station_contract))
        if not result:
            raise_404(data={"errors": "GasStationContract not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", GasStationContractResponseSchema2, summary="Получить договор с АЗС")
async def get_gas_station_contract(
    gas_station_contract: GasStationContractGetSchema = Query(...),
    gas_station_contract_service: AbsGasStationContractService = Depends(get_gas_station_contract_service),
):
    try:
        result = await gas_station_contract_service.get_gas_station_contract(pydantic_to_dto(GasStationContractDTO, gas_station_contract))
        if not result:
            raise_404(data={"errors": "GasStationContract not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", GasStationContractResponseSchema3, summary="Обновить договор с АЗС")
async def update_gas_station_contract(
    gas_station_contract: GasStationContractUpdateSchema = Body(...),
    gas_station_contract_service: AbsGasStationContractService = Depends(get_gas_station_contract_service),
):
    try:
        result = await gas_station_contract_service.update_gas_station_contract(pydantic_to_dto(GasStationContractDTO, gas_station_contract))
        if not result:
            raise_404(data={"errors": "GasStationContract not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", GasStationContractResponseSchema4, summary="Удалить договор с АЗС")
async def delete_gas_station_contract(
    gas_station_contract: GasStationContractDeleteSchema = Body(...),
    gas_station_contract_service: AbsGasStationContractService = Depends(get_gas_station_contract_service),
):
    try:
        result = await gas_station_contract_service.delete_gas_station_contract(pydantic_to_dto(GasStationContractDTO, gas_station_contract))
        if not result:
            raise_404(data={"errors": "GasStationContract not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
