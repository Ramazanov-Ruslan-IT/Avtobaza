from v1.src.db.repositories.gas_station.repo import GasStationRepo
from v1.src.db.repositories.gas_station.abs_repo import AbsGasStationRepo


async def get_gas_station_repo() -> AbsGasStationRepo:
    return GasStationRepo()
