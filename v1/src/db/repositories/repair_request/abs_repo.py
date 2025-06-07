from abc import ABC, abstractmethod

from v1.src.app.dto.repair_request import RepairRequestDTO


class AbsRepairRequestRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_repair_request(cls, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        raise NotImplementedError("create_repair_request() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_repair_request(cls, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        raise NotImplementedError("get_repair_request() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_repair_request(cls, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        raise NotImplementedError("update_repair_request() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_repair_request(cls, data: RepairRequestDTO) -> RepairRequestDTO | None | Exception:
        raise NotImplementedError("delete_repair_request() must be implemented in subclass")
