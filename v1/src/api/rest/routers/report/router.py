from datetime import datetime

from fastapi import Depends, Body, APIRouter, Query
from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.report.dependencies import get_report_service, AbsReportService
from v1.src.app.dto.report import ReportDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.report.schemas import (
    ReportCreateSchema, ReportGetSchema, ReportUpdateSchema, ReportDeleteSchema,
    ReportResponseSchema1, ReportResponseSchema2, ReportResponseSchema3, ReportResponseSchema4,
    ReportListSchema, ReportSearchSchema, ReportSearchListSchema,
    ReportExportResponseSchema, ReportStatsSchema
)

router = APIRouter(prefix="/report", tags=["Report"])

# --- CRUD ---

@api_post(router, "", ReportResponseSchema1, summary="Создать отчёт")
async def create_report(
    report: ReportCreateSchema = Body(...),
    report_service: AbsReportService = Depends(get_report_service),
):
    try:
        result = await report_service.create_report(pydantic_to_dto(ReportDTO, report))
        if not result:
            raise_404(data={"errors": "Report not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", ReportResponseSchema2, summary="Получить отчёт")
async def get_report(
    report: ReportGetSchema = Query(...),
    report_service: AbsReportService = Depends(get_report_service),
):
    try:
        result = await report_service.get_report(pydantic_to_dto(ReportDTO, report))
        if not result:
            raise_404(data={"errors": "Report not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", ReportResponseSchema3, summary="Обновить отчёт")
async def update_report(
    report: ReportUpdateSchema = Body(...),
    report_service: AbsReportService = Depends(get_report_service),
):
    try:
        result = await report_service.update_report(pydantic_to_dto(ReportDTO, report))
        if not result:
            raise_404(data={"errors": "Report not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", ReportResponseSchema4, summary="Удалить отчёт")
async def delete_report(
    report: ReportDeleteSchema = Body(...),
    report_service: AbsReportService = Depends(get_report_service),
):
    try:
        result = await report_service.delete_report(pydantic_to_dto(ReportDTO, report))
        if not result:
            raise_404(data={"errors": "Report not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

# --- Дополнительные endpoint-ы ---

@api_get(router, "/list", ReportListSchema, summary="Список всех отчётов")
async def list_reports(
    skip: int = Query(0, description="Сколько пропустить"),
    limit: int = Query(10, description="Сколько вернуть"),
):
    # Заглушка
    from datetime import datetime
    return [
        ReportResponseSchema1(
            id=str(i),
            type="refueling",
            created_by="user1",
            generated_at=datetime.now(),
            payload={"rows": 5}
        ) for i in range(skip, skip + limit)
    ]

@api_get(router, "/search", ReportSearchListSchema, summary="Поиск отчетов по фильтрам")
async def search_reports(
    type: str = Query(None),
    created_by: str = Query(None),
    date_from: datetime = Query(None),
    date_to: datetime = Query(None),
):
    # Заглушка: просто одна запись
    return [
        ReportResponseSchema1(
            id="42",
            type=type or "service",
            created_by=created_by or "user42",
            generated_at=date_from or datetime.now(),
            payload={"test": True}
        )
    ]

@api_get(router, "/{report_id}/export", ReportExportResponseSchema, summary="Выгрузить отчёт в файл")
async def export_report(report_id: str):
    from datetime import datetime, timedelta
    # Заглушка: возвращает ссылку
    return ReportExportResponseSchema(
        file_url=f"https://files.mirea.local/reports/{report_id}.xlsx",
        expires_at=datetime.now() + timedelta(hours=2)
    )

@api_get(router, "/stats", ReportStatsSchema, summary="Статистика по отчетам")
async def report_stats():
    from datetime import datetime
    return ReportStatsSchema(
        total=258,
        by_type={"refueling": 120, "service": 62, "finance": 76},
        last_report_date=datetime.now()
    )
