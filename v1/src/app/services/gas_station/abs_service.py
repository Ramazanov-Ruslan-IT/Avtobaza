from abc import ABC, abstractmethod

from v1.src.app.dto.gas_station import GasStationDTO


class AbsGasStationService(ABC):
    @abstractmethod
    async def create_gas_station(self, data: GasStationDTO) -> GasStationDTO | None | Exception:
        pass

    @abstractmethod
    async def get_gas_station(self, data: GasStationDTO) -> GasStationDTO | None | Exception:
        pass

    @abstractmethod
    async def update_gas_station(self, data: GasStationDTO) -> GasStationDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_gas_station(self, data: GasStationDTO) -> GasStationDTO | None | Exception:
        pass
