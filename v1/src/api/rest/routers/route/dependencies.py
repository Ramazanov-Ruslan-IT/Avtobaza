from fastapi import Depends

from v1.src.app.services.route import build_route_service, AbsRouteService

async def get_route_service(
    route_service: AbsRouteService = Depends(build_route_service)
) -> AbsRouteService:
    return route_service
