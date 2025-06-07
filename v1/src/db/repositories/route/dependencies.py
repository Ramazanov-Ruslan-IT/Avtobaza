from v1.src.db.repositories.route.repo import RouteRepo
from v1.src.db.repositories.route.abs_repo import AbsRouteRepo


async def get_route_repo() -> AbsRouteRepo:
    return RouteRepo()
