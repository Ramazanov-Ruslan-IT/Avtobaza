from v1.src.app.services.gas_station_fuel.abs_service import AbsGasStationFuelService
from v1.src.db.repositories.gas_station_fuel import AbsGasStationFuelRepo
from v1.src.app.dto.gas_station_fuel import GasStationFuelDTO


class GasStationFuelService(AbsGasStationFuelService):
    def __init__(self, gas_station_fuel_repo: AbsGasStationFuelRepo):
        self.gas_station_fuel_repo = gas_station_fuel_repo

    async def create_gas_station_fuel(self, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        return await self.gas_station_fuel_repo.create_gas_station_fuel(data)

    async def get_gas_station_fuel(self, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        result = await self.gas_station_fuel_repo.get_gas_station_fuel(data)
        if not result:
            raise ValueError("Gas station fuel not found")
        return result

    async def update_gas_station_fuel(self, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        result = await self.gas_station_fuel_repo.update_gas_station_fuel(data)
        if not result:
            raise ValueError("Cannot update: gas station fuel not found")
        return result

    async def delete_gas_station_fuel(self, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        result = await self.gas_station_fuel_repo.delete_gas_station_fuel(data)
        if not result:
            raise ValueError("Cannot delete: gas station fuel not found")
        return result
