from abc import ABC, abstractmethod

from v1.src.app.dto.gas_station_contract import GasStationContractDTO


class AbsGasStationContractRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_gas_station_contract(cls, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        raise NotImplementedError("create_gas_station_contract() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_gas_station_contract(cls, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        raise NotImplementedError("get_gas_station_contract() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_gas_station_contract(cls, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        raise NotImplementedError("update_gas_station_contract() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_gas_station_contract(cls, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        raise NotImplementedError("delete_gas_station_contract() must be implemented in subclass")
