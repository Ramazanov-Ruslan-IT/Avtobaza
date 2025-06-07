from fastapi import Depends

from v1.src.app.services.supplier import build_supplier_service, AbsSupplierService

async def get_supplier_service(
    supplier_service: AbsSupplierService = Depends(build_supplier_service)
) -> AbsSupplierService:
    return supplier_service
