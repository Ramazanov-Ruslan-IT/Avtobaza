from fastapi import Depends

from v1.src.app.services.user import build_user_service, AbsUserService

async def get_user_service(
    user_service: AbsUserService = Depends(build_user_service)
) -> AbsUserService:
    return user_service
