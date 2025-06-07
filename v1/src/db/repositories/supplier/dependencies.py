from v1.src.db.repositories.supplier.repo import SupplierRepo
from v1.src.db.repositories.supplier.abs_repo import AbsSupplierRepo


async def get_supplier_repo() -> AbsSupplierRepo:
    return SupplierRepo()
