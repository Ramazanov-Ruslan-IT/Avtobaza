from v1.src.app.services.gas_station.abs_service import AbsGasStationService
from v1.src.db.repositories.gas_station import AbsGasStationRepo
from v1.src.app.dto.gas_station import GasStationDTO


class GasStationService(AbsGasStationService):
    def __init__(self, gas_station_repo: AbsGasStationRepo):
        self.gas_station_repo = gas_station_repo

    async def create_gas_station(self, data: GasStationDTO) -> GasStationDTO | None | Exception:
        return await self.gas_station_repo.create_gas_station(data)

    async def get_gas_station(self, data: GasStationDTO) -> GasStationDTO | None | Exception:
        result = await self.gas_station_repo.get_gas_station(data)
        if not result:
            raise ValueError("Gas station not found")
        return result

    async def update_gas_station(self, data: GasStationDTO) -> GasStationDTO | None | Exception:
        result = await self.gas_station_repo.update_gas_station(data)
        if not result:
            raise ValueError("Cannot update: gas station not found")
        return result

    async def delete_gas_station(self, data: GasStationDTO) -> GasStationDTO | None | Exception:
        result = await self.gas_station_repo.delete_gas_station(data)
        if not result:
            raise ValueError("Cannot delete: gas station not found")
        return result
