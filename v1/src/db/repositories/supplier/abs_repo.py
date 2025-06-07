from abc import ABC, abstractmethod

from v1.src.app.dto.supplier import SupplierDTO


class AbsSupplierRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_supplier(cls, data: SupplierDTO) -> SupplierDTO | None | Exception:
        raise NotImplementedError("create_supplier() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_supplier(cls, data: SupplierDTO) -> SupplierDTO | None | Exception:
        raise NotImplementedError("get_supplier() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_supplier(cls, data: SupplierDTO) -> SupplierDTO | None | Exception:
        raise NotImplementedError("update_supplier() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_supplier(cls, data: SupplierDTO) -> SupplierDTO | None | Exception:
        raise NotImplementedError("delete_supplier() must be implemented in subclass")
