from fastapi import Depends

from v1.src.app.services.autobase import build_autobase_service, AbsAutobaseService

async def get_autobase_service(autobase_service: AbsAutobaseService = Depends(build_autobase_service)) -> AbsAutobaseService:
    return autobase_service
