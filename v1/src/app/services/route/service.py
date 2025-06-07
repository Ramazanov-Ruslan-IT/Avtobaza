from v1.src.app.services.route.abs_service import AbsRouteService
from v1.src.db.repositories.route import AbsRouteRepo
from v1.src.app.dto.route import RouteDTO


class RouteService(AbsRouteService):
    def __init__(self, route_repo: AbsRouteRepo):
        self.route_repo = route_repo

    async def create_route(self, data: RouteDTO) -> RouteDTO | None | Exception:
        return await self.route_repo.create_route(data)

    async def get_route(self, data: RouteDTO) -> RouteDTO | None | Exception:
        result = await self.route_repo.get_route(data)
        if not result:
            raise ValueError("Route not found")
        return result

    async def update_route(self, data: RouteDTO) -> RouteDTO | None | Exception:
        result = await self.route_repo.update_route(data)
        if not result:
            raise ValueError("Cannot update: route not found")
        return result

    async def delete_route(self, data: RouteDTO) -> RouteDTO | None | Exception:
        result = await self.route_repo.delete_route(data)
        if not result:
            raise ValueError("Cannot delete: route not found")
        return result
