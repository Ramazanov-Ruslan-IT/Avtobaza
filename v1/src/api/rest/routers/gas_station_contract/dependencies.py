from fastapi import Depends

from v1.src.app.services.gas_station_contract import build_gas_station_contract_service, AbsGasStationContractService


async def get_gas_station_contract_service(
    gas_station_contract_service: AbsGasStationContractService = Depends(build_gas_station_contract_service)
) -> AbsGasStationContractService:
    return gas_station_contract_service
