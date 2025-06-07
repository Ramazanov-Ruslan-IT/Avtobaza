from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.document.dependencies import get_document_service, AbsDocumentService
from v1.src.app.dto.document import DocumentDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.document.schemas import (
    DocumentCreateSchema, DocumentGetSchema, DocumentUpdateSchema, DocumentDeleteSchema,
    DocumentResponseSchema1, DocumentResponseSchema2, DocumentResponseSchema3, DocumentResponseSchema4
)

router = APIRouter(prefix="/document", tags=["Document"])

@api_post(router, "", DocumentResponseSchema1, summary="Создать документ")
async def create_document(
    document: DocumentCreateSchema = Body(...),
    document_service: AbsDocumentService = Depends(get_document_service),
):
    try:
        result = await document_service.create_document(pydantic_to_dto(DocumentDTO, document))
        if not result:
            raise_404(data={"errors": "Document not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", DocumentResponseSchema2, summary="Получить документ")
async def get_document(
    document: DocumentGetSchema = Query(...),
    document_service: AbsDocumentService = Depends(get_document_service),
):
    try:
        result = await document_service.get_document(pydantic_to_dto(DocumentDTO, document))
        if not result:
            raise_404(data={"errors": "Document not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", DocumentResponseSchema3, summary="Обновить документ")
async def update_document(
    document: DocumentUpdateSchema = Body(...),
    document_service: AbsDocumentService = Depends(get_document_service),
):
    try:
        result = await document_service.update_document(pydantic_to_dto(DocumentDTO, document))
        if not result:
            raise_404(data={"errors": "Document not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", DocumentResponseSchema4, summary="Удалить документ")
async def delete_document(
    document: DocumentDeleteSchema = Body(...),
    document_service: AbsDocumentService = Depends(get_document_service),
):
    try:
        result = await document_service.delete_document(pydantic_to_dto(DocumentDTO, document))
        if not result:
            raise_404(data={"errors": "Document not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
