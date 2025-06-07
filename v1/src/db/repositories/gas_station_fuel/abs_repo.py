from abc import ABC, abstractmethod

from v1.src.app.dto.gas_station_fuel import GasStationFuelDTO


class AbsGasStationFuelRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_gas_station_fuel(cls, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        raise NotImplementedError("create_gas_station_fuel() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_gas_station_fuel(cls, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        raise NotImplementedError("get_gas_station_fuel() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_gas_station_fuel(cls, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        raise NotImplementedError("update_gas_station_fuel() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_gas_station_fuel(cls, data: GasStationFuelDTO) -> GasStationFuelDTO | None | Exception:
        raise NotImplementedError("delete_gas_station_fuel() must be implemented in subclass")
