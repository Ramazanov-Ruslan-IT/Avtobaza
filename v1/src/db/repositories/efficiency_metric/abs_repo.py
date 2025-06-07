from abc import ABC, abstractmethod

from v1.src.app.dto.efficiency_metric import EfficiencyMetricDTO


class AbsEfficiencyMetricRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_efficiency_metric(cls, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        raise NotImplementedError("create_efficiency_metric() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_efficiency_metric(cls, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        raise NotImplementedError("get_efficiency_metric() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_efficiency_metric(cls, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        raise NotImplementedError("update_efficiency_metric() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_efficiency_metric(cls, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        raise NotImplementedError("delete_efficiency_metric() must be implemented in subclass")
