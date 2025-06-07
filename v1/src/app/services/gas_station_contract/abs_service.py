from abc import ABC, abstractmethod

from v1.src.app.dto.gas_station_contract import GasStationContractDTO


class AbsGasStationContractService(ABC):
    @abstractmethod
    async def create_gas_station_contract(self, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        pass

    @abstractmethod
    async def get_gas_station_contract(self, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        pass

    @abstractmethod
    async def update_gas_station_contract(self, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_gas_station_contract(self, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        pass
