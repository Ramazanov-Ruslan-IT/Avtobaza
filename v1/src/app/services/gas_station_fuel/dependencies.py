from v1.src.app.services.gas_station_fuel.abs_service import AbsGasStationFuelService
from v1.src.app.services.gas_station_fuel.service import GasStationFuelService

from v1.src.db.repositories.gas_station_fuel.dependencies import get_gas_station_fuel_repo


async def build_gas_station_fuel_service() -> AbsGasStationFuelService:
    gas_station_fuel_repo = await get_gas_station_fuel_repo()
    return GasStationFuelService(gas_station_fuel_repo)
