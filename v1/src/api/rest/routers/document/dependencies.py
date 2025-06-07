from fastapi import Depends

from v1.src.app.services.document import build_document_service, AbsDocumentService

async def get_document_service(document_service: AbsDocumentService = Depends(build_document_service)) -> AbsDocumentService:
    return document_service
