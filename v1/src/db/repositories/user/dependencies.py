from v1.src.db.repositories.user.repo import UserRepo
from v1.src.db.repositories.user.abs_repo import AbsUserRepo


async def get_user_repo() -> AbsUserRepo:
    return UserRepo()
