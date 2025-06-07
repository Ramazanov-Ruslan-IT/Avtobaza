from abc import ABC, abstractmethod

from v1.src.app.dto.supplier import SupplierDTO


class AbsSupplierService(ABC):
    @abstractmethod
    async def create_supplier(self, data: SupplierDTO) -> SupplierDTO | None | Exception:
        pass

    @abstractmethod
    async def get_supplier(self, data: SupplierDTO) -> SupplierDTO | None | Exception:
        pass

    @abstractmethod
    async def update_supplier(self, data: SupplierDTO) -> SupplierDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_supplier(self, data: SupplierDTO) -> SupplierDTO | None | Exception:
        pass
