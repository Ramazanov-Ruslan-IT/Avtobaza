from v1.src.db.repositories.report.repo import ReportRepo
from v1.src.db.repositories.report.abs_repo import AbsReportRepo


async def get_report_repo() -> AbsReportRepo:
    return ReportRepo()
