from v1.src.app.services.gas_station.abs_service import AbsGasStationService
from v1.src.app.services.gas_station.service import GasStationService

from v1.src.db.repositories.gas_station.dependencies import get_gas_station_repo


async def build_gas_station_service() -> AbsGasStationService:
    gas_station_repo = await get_gas_station_repo()
    return GasStationService(gas_station_repo)
