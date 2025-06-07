from v1.src.db.repositories.gas_station_fuel.repo import GasStationFuelRepo
from v1.src.db.repositories.gas_station_fuel.abs_repo import AbsGasStationFuelRepo


async def get_gas_station_fuel_repo() -> AbsGasStationFuelRepo:
    return GasStationFuelRepo()
