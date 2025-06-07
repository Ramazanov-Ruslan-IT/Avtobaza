from abc import ABC, abstractmethod

from v1.src.app.dto.route import RouteDTO


class AbsRouteRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_route(cls, data: RouteDTO) -> RouteDTO | None | Exception:
        raise NotImplementedError("create_route() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_route(cls, data: RouteDTO) -> RouteDTO | None | Exception:
        raise NotImplementedError("get_route() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_route(cls, data: RouteDTO) -> RouteDTO | None | Exception:
        raise NotImplementedError("update_route() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_route(cls, data: RouteDTO) -> RouteDTO | None | Exception:
        raise NotImplementedError("delete_route() must be implemented in subclass")
