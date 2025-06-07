from v1.src.app.services.user.abs_service import AbsUserService
from v1.src.app.services.user.service import UserService

from v1.src.db.repositories.user.dependencies import get_user_repo


async def build_user_service() -> AbsUserService:
    user_repo = await get_user_repo()
    return UserService(user_repo)
