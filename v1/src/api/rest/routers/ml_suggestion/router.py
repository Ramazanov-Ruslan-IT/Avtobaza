from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.ml_suggestion.dependencies import get_ml_suggestion_service, AbsMlSuggestionService
from v1.src.app.dto.ml_suggestion import MlSuggestionDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.ml_suggestion.schemas import (
    MlSuggestionCreateSchema, MlSuggestionGetSchema, MlSuggestionUpdateSchema, MlSuggestionDeleteSchema,
    MlSuggestionResponseSchema1, MlSuggestionResponseSchema2, MlSuggestionResponseSchema3, MlSuggestionResponseSchema4
)

router = APIRouter(prefix="/ml_suggestion", tags=["MlSuggestion"])

@api_post(router, "", MlSuggestionResponseSchema1, summary="Создать ML-подсказку")
async def create_ml_suggestion(
    ml_suggestion: MlSuggestionCreateSchema = Body(...),
    ml_suggestion_service: AbsMlSuggestionService = Depends(get_ml_suggestion_service),
):
    try:
        result = await ml_suggestion_service.create_ml_suggestion(pydantic_to_dto(MlSuggestionDTO, ml_suggestion))
        if not result:
            raise_404(data={"errors": "MlSuggestion not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", MlSuggestionResponseSchema2, summary="Получить ML-подсказку")
async def get_ml_suggestion(
    ml_suggestion: MlSuggestionGetSchema = Query(...),
    ml_suggestion_service: AbsMlSuggestionService = Depends(get_ml_suggestion_service),
):
    try:
        result = await ml_suggestion_service.get_ml_suggestion(pydantic_to_dto(MlSuggestionDTO, ml_suggestion))
        if not result:
            raise_404(data={"errors": "MlSuggestion not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", MlSuggestionResponseSchema3, summary="Обновить ML-подсказку")
async def update_ml_suggestion(
    ml_suggestion: MlSuggestionUpdateSchema = Body(...),
    ml_suggestion_service: AbsMlSuggestionService = Depends(get_ml_suggestion_service),
):
    try:
        result = await ml_suggestion_service.update_ml_suggestion(pydantic_to_dto(MlSuggestionDTO, ml_suggestion))
        if not result:
            raise_404(data={"errors": "MlSuggestion not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", MlSuggestionResponseSchema4, summary="Удалить ML-подсказку")
async def delete_ml_suggestion(
    ml_suggestion: MlSuggestionDeleteSchema = Body(...),
    ml_suggestion_service: AbsMlSuggestionService = Depends(get_ml_suggestion_service),
):
    try:
        result = await ml_suggestion_service.delete_ml_suggestion(pydantic_to_dto(MlSuggestionDTO, ml_suggestion))
        if not result:
            raise_404(data={"errors": "MlSuggestion not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
