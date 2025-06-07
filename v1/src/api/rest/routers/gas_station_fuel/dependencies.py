from fastapi import Depends

from v1.src.app.services.gas_station_fuel import build_gas_station_fuel_service, AbsGasStationFuelService

async def get_gas_station_fuel_service(
    gas_station_fuel_service: AbsGasStationFuelService = Depends(build_gas_station_fuel_service)
) -> AbsGasStationFuelService:
    return gas_station_fuel_service
