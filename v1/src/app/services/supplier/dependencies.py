from v1.src.app.services.supplier.abs_service import AbsSupplierService
from v1.src.app.services.supplier.service import SupplierService

from v1.src.db.repositories.supplier.dependencies import get_supplier_repo


async def build_supplier_service() -> AbsSupplierService:
    supplier_repo = await get_supplier_repo()
    return SupplierService(supplier_repo)
