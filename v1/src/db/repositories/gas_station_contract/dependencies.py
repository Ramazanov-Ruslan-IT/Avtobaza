from v1.src.db.repositories.gas_station_contract.repo import GasStationContractRepo
from v1.src.db.repositories.gas_station_contract.abs_repo import AbsGasStationContractRepo


async def get_gas_station_contract_repo() -> AbsGasStationContractRepo:
    return GasStationContractRepo()
