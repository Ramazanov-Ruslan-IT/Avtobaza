from v1.src.app.services.efficiency_metric.abs_service import AbsEfficiencyMetricService
from v1.src.app.services.efficiency_metric.service import EfficiencyMetricService

from v1.src.db.repositories.efficiency_metric.dependencies import get_efficiency_metric_repo


async def build_efficiency_metric_service() -> AbsEfficiencyMetricService:
    efficiency_metric_repo = await get_efficiency_metric_repo()
    return EfficiencyMetricService(efficiency_metric_repo)
