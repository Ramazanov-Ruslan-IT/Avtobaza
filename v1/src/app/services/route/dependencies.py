from v1.src.app.services.route.abs_service import AbsRouteService
from v1.src.app.services.route.service import RouteService

from v1.src.db.repositories.route.dependencies import get_route_repo


async def build_route_service() -> AbsRouteService:
    route_repo = await get_route_repo()
    return RouteService(route_repo)
