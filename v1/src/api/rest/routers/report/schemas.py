from datetime import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict

# --- CRUD ---

class ReportCreateSchema(BaseModel):
    type: str
    created_by: str
    generated_at: datetime
    payload: dict[str, Any]
    model_config = ConfigDict(from_attributes=True)

class ReportGetSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class ReportUpdateSchema(BaseModel):
    id: str
    type: str | None = None
    created_by: str | None = None
    generated_at: datetime | None = None
    payload: dict[str, Any] | None = None
    model_config = ConfigDict(from_attributes=True)

class ReportDeleteSchema(BaseModel):
    id: str
    model_config = ConfigDict(from_attributes=True)

class ReportResponseSchema1(BaseModel):
    id: str
    type: str
    created_by: str
    generated_at: datetime
    payload: dict[str, Any]
    model_config = ConfigDict(from_attributes=True)

class ReportResponseSchema2(ReportResponseSchema1): pass
class ReportResponseSchema3(ReportResponseSchema1): pass
class ReportResponseSchema4(ReportResponseSchema1): pass

# --- Расширенные схемы ---

# Для списка отчетов
ReportListSchema = list[ReportResponseSchema1]

# Для поиска по типу/дате/автору
class ReportSearchSchema(BaseModel):
    type: str | None = None
    created_by: str | None = None
    date_from: datetime | None = None
    date_to: datetime | None = None
    model_config = ConfigDict(from_attributes=True)
ReportSearchListSchema = list[ReportResponseSchema1]

# Для выгрузки отчета в файл
class ReportExportResponseSchema(BaseModel):
    file_url: str
    expires_at: datetime
    model_config = ConfigDict(from_attributes=True)

# Для статистики по отчетам
class ReportStatsSchema(BaseModel):
    total: int
    by_type: dict[str, int]
    last_report_date: datetime
    model_config = ConfigDict(from_attributes=True)
