from v1.src.app.services.ml_suggestion.abs_service import AbsMlSuggestionService
from v1.src.db.repositories.ml_suggestion import AbsMlSuggestionRepo
from v1.src.app.dto.ml_suggestion import MlSuggestionDTO


class MlSuggestionService(AbsMlSuggestionService):
    def __init__(self, ml_suggestion_repo: AbsMlSuggestionRepo):
        self.ml_suggestion_repo = ml_suggestion_repo

    async def create_ml_suggestion(self, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        return await self.ml_suggestion_repo.create_ml_suggestion(data)

    async def get_ml_suggestion(self, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        result = await self.ml_suggestion_repo.get_ml_suggestion(data)
        if not result:
            raise ValueError("ML suggestion not found")
        return result

    async def update_ml_suggestion(self, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        result = await self.ml_suggestion_repo.update_ml_suggestion(data)
        if not result:
            raise ValueError("Cannot update: ML suggestion not found")
        return result

    async def delete_ml_suggestion(self, data: MlSuggestionDTO) -> MlSuggestionDTO | None | Exception:
        result = await self.ml_suggestion_repo.delete_ml_suggestion(data)
        if not result:
            raise ValueError("Cannot delete: ML suggestion not found")
        return result
