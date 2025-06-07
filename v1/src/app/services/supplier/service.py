from v1.src.app.services.supplier.abs_service import AbsSupplierService
from v1.src.db.repositories.supplier import AbsSupplierRepo
from v1.src.app.dto.supplier import SupplierDTO


class SupplierService(AbsSupplierService):
    def __init__(self, supplier_repo: AbsSupplierRepo):
        self.supplier_repo = supplier_repo

    async def create_supplier(self, data: SupplierDTO) -> SupplierDTO | None | Exception:
        return await self.supplier_repo.create_supplier(data)

    async def get_supplier(self, data: SupplierDTO) -> SupplierDTO | None | Exception:
        result = await self.supplier_repo.get_supplier(data)
        if not result:
            raise ValueError("Supplier not found")
        return result

    async def update_supplier(self, data: SupplierDTO) -> SupplierDTO | None | Exception:
        result = await self.supplier_repo.update_supplier(data)
        if not result:
            raise ValueError("Cannot update: supplier not found")
        return result

    async def delete_supplier(self, data: SupplierDTO) -> SupplierDTO | None | Exception:
        result = await self.supplier_repo.delete_supplier(data)
        if not result:
            raise ValueError("Cannot delete: supplier not found")
        return result
