from v1.src.app.services.report.abs_service import AbsReportService
from v1.src.app.services.report.service import ReportService

from v1.src.db.repositories.report.dependencies import get_report_repo


async def build_report_service() -> AbsReportService:
    report_repo = await get_report_repo()
    return ReportService(report_repo)
