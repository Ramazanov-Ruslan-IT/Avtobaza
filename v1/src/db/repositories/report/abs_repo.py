from abc import ABC, abstractmethod

from v1.src.app.dto.report import ReportDTO


class AbsReportRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_report(cls, data: ReportDTO) -> ReportDTO | None | Exception:
        raise NotImplementedError("create_report() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_report(cls, data: ReportDTO) -> ReportDTO | None | Exception:
        raise NotImplementedError("get_report() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_report(cls, data: ReportDTO) -> ReportDTO | None | Exception:
        raise NotImplementedError("update_report() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_report(cls, data: ReportDTO) -> ReportDTO | None | Exception:
        raise NotImplementedError("delete_report() must be implemented in subclass")
