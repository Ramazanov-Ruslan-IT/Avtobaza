from v1.src.db.repositories.efficiency_metric.repo import EfficiencyMetricRepo
from v1.src.db.repositories.efficiency_metric.abs_repo import AbsEfficiencyMetricRepo


async def get_efficiency_metric_repo() -> AbsEfficiencyMetricRepo:
    return EfficiencyMetricRepo()
