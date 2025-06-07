from abc import ABC, abstractmethod

from v1.src.app.dto.efficiency_metric import EfficiencyMetricDTO


class AbsEfficiencyMetricService(ABC):
    @abstractmethod
    async def create_efficiency_metric(self, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        pass

    @abstractmethod
    async def get_efficiency_metric(self, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        pass

    @abstractmethod
    async def update_efficiency_metric(self, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_efficiency_metric(self, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        pass
