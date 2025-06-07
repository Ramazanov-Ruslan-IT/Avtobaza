from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.report.dependencies import get_report_service, AbsReportService
from v1.src.app.dto.report import ReportDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.report.schemas import (
    ReportCreateSchema, ReportGetSchema, ReportUpdateSchema, ReportDeleteSchema,
    ReportResponseSchema1, ReportResponseSchema2, ReportResponseSchema3, ReportResponseSchema4
)

router = APIRouter(prefix="/report", tags=["Report"])

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
