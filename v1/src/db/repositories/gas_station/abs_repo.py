from abc import ABC, abstractmethod

from v1.src.app.dto.gas_station import GasStationDTO


class AbsGasStationRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_gas_station(cls, data: GasStationDTO) -> GasStationDTO | None | Exception:
        raise NotImplementedError("create_gas_station() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_gas_station(cls, data: GasStationDTO) -> GasStationDTO | None | Exception:
        raise NotImplementedError("get_gas_station() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_gas_station(cls, data: GasStationDTO) -> GasStationDTO | None | Exception:
        raise NotImplementedError("update_gas_station() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_gas_station(cls, data: GasStationDTO) -> GasStationDTO | None | Exception:
        raise NotImplementedError("delete_gas_station() must be implemented in subclass")
