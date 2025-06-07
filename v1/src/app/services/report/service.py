from v1.src.app.services.report.abs_service import AbsReportService
from v1.src.db.repositories.report import AbsReportRepo
from v1.src.app.dto.report import ReportDTO


class ReportService(AbsReportService):
    def __init__(self, report_repo: AbsReportRepo):
        self.report_repo = report_repo

    async def create_report(self, data: ReportDTO) -> ReportDTO | None | Exception:
        return await self.report_repo.create_report(data)

    async def get_report(self, data: ReportDTO) -> ReportDTO | None | Exception:
        result = await self.report_repo.get_report(data)
        if not result:
            raise ValueError("Report not found")
        return result

    async def update_report(self, data: ReportDTO) -> ReportDTO | None | Exception:
        result = await self.report_repo.update_report(data)
        if not result:
            raise ValueError("Cannot update: report not found")
        return result

    async def delete_report(self, data: ReportDTO) -> ReportDTO | None | Exception:
        result = await self.report_repo.delete_report(data)
        if not result:
            raise ValueError("Cannot delete: report not found")
        return result
