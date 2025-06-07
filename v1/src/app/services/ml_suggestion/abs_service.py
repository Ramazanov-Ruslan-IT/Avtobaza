from abc import ABC, abstractmethod

from v1.src.app.dto.ml_suggestion import MlSuggestionDTO


class AbsMlSuggestionService(ABC):
    @abstractmethod
    async def create_ml_suggestion(self, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        pass

    @abstractmethod
    async def get_ml_suggestion(self, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        pass

    @abstractmethod
    async def update_ml_suggestion(self, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_ml_suggestion(self, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        pass
