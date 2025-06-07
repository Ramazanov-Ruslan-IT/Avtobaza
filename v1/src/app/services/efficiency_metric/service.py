from v1.src.app.services.efficiency_metric.abs_service import AbsEfficiencyMetricService
from v1.src.db.repositories.efficiency_metric import AbsEfficiencyMetricRepo
from v1.src.app.dto.efficiency_metric import EfficiencyMetricDTO


class EfficiencyMetricService(AbsEfficiencyMetricService):
    def __init__(self, efficiency_metric_repo: AbsEfficiencyMetricRepo):
        self.efficiency_metric_repo = efficiency_metric_repo

    async def create_efficiency_metric(self, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        return await self.efficiency_metric_repo.create_efficiency_metric(data)

    async def get_efficiency_metric(self, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        result = await self.efficiency_metric_repo.get_efficiency_metric(data)
        if not result:
            raise ValueError("Efficiency metric not found")
        return result

    async def update_efficiency_metric(self, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        result = await self.efficiency_metric_repo.update_efficiency_metric(data)
        if not result:
            raise ValueError("Cannot update: efficiency metric not found")
        return result

    async def delete_efficiency_metric(self, data: EfficiencyMetricDTO) -> EfficiencyMetricDTO | None | Exception:
        result = await self.efficiency_metric_repo.delete_efficiency_metric(data)
        if not result:
            raise ValueError("Cannot delete: efficiency metric not found")
        return result
