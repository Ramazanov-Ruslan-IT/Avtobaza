from fastapi import Depends

from v1.src.app.services.ml_suggestion import build_ml_suggestion_service, AbsMlSuggestionService


async def get_ml_suggestion_service(
    ml_suggestion_service: AbsMlSuggestionService = Depends(build_ml_suggestion_service)
) -> AbsMlSuggestionService:
    return ml_suggestion_service
