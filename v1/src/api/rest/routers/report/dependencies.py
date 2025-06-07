from fastapi import Depends

from v1.src.app.services.report import build_report_service, AbsReportService

async def get_report_service(
    report_service: AbsReportService = Depends(build_report_service)
) -> AbsReportService:
    return report_service
