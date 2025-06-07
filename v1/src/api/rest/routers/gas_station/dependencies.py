from fastapi import Depends

from v1.src.app.services.gas_station import build_gas_station_service, AbsGasStationService

async def get_gas_station_service(
    gas_station_service: AbsGasStationService = Depends(build_gas_station_service)
) -> AbsGasStationService:
    return gas_station_service
