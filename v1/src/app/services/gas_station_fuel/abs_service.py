from abc import ABC, abstractmethod

from v1.src.app.dto.gas_station_fuel import GasStationFuelDTO


class AbsGasStationFuelService(ABC):
    @abstractmethod
    async def create_gas_station_fuel(self, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        pass

    @abstractmethod
    async def get_gas_station_fuel(self, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        pass

    @abstractmethod
    async def update_gas_station_fuel(self, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_gas_station_fuel(self, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        pass
