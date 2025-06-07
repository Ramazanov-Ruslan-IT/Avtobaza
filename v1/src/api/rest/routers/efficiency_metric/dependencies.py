from fastapi import Depends

from v1.src.app.services.efficiency_metric import build_efficiency_metric_service, AbsEfficiencyMetricService

async def get_efficiency_metric_service(
    efficiency_metric_service: AbsEfficiencyMetricService = Depends(build_efficiency_metric_service)
) -> AbsEfficiencyMetricService:
    return efficiency_metric_service
