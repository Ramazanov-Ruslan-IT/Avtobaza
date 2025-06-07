from v1.src.app.services.gas_station_contract.abs_service import AbsGasStationContractService
from v1.src.app.services.gas_station_contract.service import GasStationContractService

from v1.src.db.repositories.gas_station_contract.dependencies import get_gas_station_contract_repo


async def build_gas_station_contract_service() -> AbsGasStationContractService:
    gas_station_contract_repo = await get_gas_station_contract_repo()
    return GasStationContractService(gas_station_contract_repo)
