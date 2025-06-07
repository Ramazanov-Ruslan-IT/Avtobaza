from v1.src.app.services.access_log.abs_service import AbsAccessLogService
from v1.src.db.repositories.access_log import AbsAccessLogRepo
from v1.src.app.dto.access_log import AccessLogDTO


class AccessLogService(AbsAccessLogService):
    def __init__(self, access_log_repo: AbsAccessLogRepo):
        self.access_log_repo = access_log_repo

    async def create_access_log(self, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        return await self.access_log_repo.create_access_log(data)

    async def get_access_log(self, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        result = await self.access_log_repo.get_access_log(data)
        if not result:
            raise ValueError("Access log not found")
        return result

    async def update_access_log(self, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        result = await self.access_log_repo.update_access_log(data)
        if not result:
            raise ValueError("Cannot update: access log not found")
        return result

    async def delete_access_log(self, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        result = await self.access_log_repo.delete_access_log(data)
        if not result:
            raise ValueError("Cannot delete: access log not found")
        return result
