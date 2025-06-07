from v1.src.app.services.gas_station_contract.abs_service import AbsGasStationContractService
from v1.src.db.repositories.gas_station_contract import AbsGasStationContractRepo
from v1.src.app.dto.gas_station_contract import GasStationContractDTO


class GasStationContractService(AbsGasStationContractService):
    def __init__(self, gas_station_contract_repo: AbsGasStationContractRepo):
        self.gas_station_contract_repo = gas_station_contract_repo

    async def create_gas_station_contract(self, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        return await self.gas_station_contract_repo.create_gas_station_contract(data)

    async def get_gas_station_contract(self, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        result = await self.gas_station_contract_repo.get_gas_station_contract(data)
        if not result:
            raise ValueError("Gas station contract not found")
        return result

    async def update_gas_station_contract(self, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        result = await self.gas_station_contract_repo.update_gas_station_contract(data)
        if not result:
            raise ValueError("Cannot update: gas station contract not found")
        return result

    async def delete_gas_station_contract(self, data: GasStationContractDTO) -> GasStationContractDTO | None | Exception:
        result = await self.gas_station_contract_repo.delete_gas_station_contract(data)
        if not result:
            raise ValueError("Cannot delete: gas station contract not found")
        return result
