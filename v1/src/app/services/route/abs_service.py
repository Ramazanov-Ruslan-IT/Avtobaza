from abc import ABC, abstractmethod

from v1.src.app.dto.route import RouteDTO


class AbsRouteService(ABC):
    @abstractmethod
    async def create_route(self, data: RouteDTO) -> RouteDTO | None | Exception:
        pass

    @abstractmethod
    async def get_route(self, data: RouteDTO) -> RouteDTO | None | Exception:
        pass

    @abstractmethod
    async def update_route(self, data: RouteDTO) -> RouteDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_route(self, data: RouteDTO) -> RouteDTO | None | Exception:
        pass
