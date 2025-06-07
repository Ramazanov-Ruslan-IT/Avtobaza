from v1.src.app.services.user.abs_service import AbsUserService
from v1.src.db.repositories.user import AbsUserRepo
from v1.src.app.dto.user import UserDTO


class UserService(AbsUserService):
    def __init__(self, user_repo: AbsUserRepo):
        self.user_repo = user_repo

    async def create_user(self, data: UserDTO) -> UserDTO | None | Exception:
        return await self.user_repo.create_user(data)

    async def get_user(self, data: UserDTO) -> UserDTO | None | Exception:
        result = await self.user_repo.get_user(data)
        if not result:
            raise ValueError("User not found")
        return result

    async def update_user(self, data: UserDTO) -> UserDTO | None | Exception:
        result = await self.user_repo.update_user(data)
        if not result:
            raise ValueError("Cannot update: user not found")
        return result

    async def delete_user(self, data: UserDTO) -> UserDTO | None | Exception:
        result = await self.user_repo.delete_user(data)
        if not result:
            raise ValueError("Cannot delete: user not found")
        return result
