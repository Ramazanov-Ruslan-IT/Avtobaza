from abc import ABC, abstractmethod

from v1.src.app.dto.report import ReportDTO


class AbsReportService(ABC):
    @abstractmethod
    async def create_report(self, data: ReportDTO) -> ReportDTO | None | Exception:
        pass

    @abstractmethod
    async def get_report(self, data: ReportDTO) -> ReportDTO | None | Exception:
        pass

    @abstractmethod
    async def update_report(self, data: ReportDTO) -> ReportDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_report(self, data: ReportDTO) -> ReportDTO | None | Exception:
        pass
