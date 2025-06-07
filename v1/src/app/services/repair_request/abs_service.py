from abc import ABC, abstractmethod

from v1.src.app.dto.repair_request import RepairRequestDTO


class AbsRepairRequestService(ABC):
    @abstractmethod
    async def create_repair_request(self, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        pass

    @abstractmethod
    async def get_repair_request(self, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        pass

    @abstractmethod
    async def update_repair_request(self, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_repair_request(self, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        pass
