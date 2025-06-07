from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.financial_transaction.dependencies import get_financial_transaction_service, AbsFinancialTransactionService
from v1.src.app.dto.financial_transaction import FinancialTransactionDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.financial_transaction.schemas import (
    FinancialTransactionCreateSchema, FinancialTransactionGetSchema, FinancialTransactionUpdateSchema, FinancialTransactionDeleteSchema,
    FinancialTransactionResponseSchema1, FinancialTransactionResponseSchema2, FinancialTransactionResponseSchema3, FinancialTransactionResponseSchema4
)

router = APIRouter(prefix="/financial_transaction", tags=["FinancialTransaction"])

@api_post(router, "", FinancialTransactionResponseSchema1, summary="Создать финансовую транзакцию")
async def create_financial_transaction(
    financial_transaction: FinancialTransactionCreateSchema = Body(...),
    financial_transaction_service: AbsFinancialTransactionService = Depends(get_financial_transaction_service),
):
    try:
        result = await financial_transaction_service.create_financial_transaction(pydantic_to_dto(FinancialTransactionDTO, financial_transaction))
        if not result:
            raise_404(data={"errors": "FinancialTransaction not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", FinancialTransactionResponseSchema2, summary="Получить финансовую транзакцию")
async def get_financial_transaction(
    financial_transaction: FinancialTransactionGetSchema = Query(...),
    financial_transaction_service: AbsFinancialTransactionService = Depends(get_financial_transaction_service),
):
    try:
        result = await financial_transaction_service.get_financial_transaction(pydantic_to_dto(FinancialTransactionDTO, financial_transaction))
        if not result:
            raise_404(data={"errors": "FinancialTransaction not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", FinancialTransactionResponseSchema3, summary="Обновить финансовую транзакцию")
async def update_financial_transaction(
    financial_transaction: FinancialTransactionUpdateSchema = Body(...),
    financial_transaction_service: AbsFinancialTransactionService = Depends(get_financial_transaction_service),
):
    try:
        result = await financial_transaction_service.update_financial_transaction(pydantic_to_dto(FinancialTransactionDTO, financial_transaction))
        if not result:
            raise_404(data={"errors": "FinancialTransaction not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", FinancialTransactionResponseSchema4, summary="Удалить финансовую транзакцию")
async def delete_financial_transaction(
    financial_transaction: FinancialTransactionDeleteSchema = Body(...),
    financial_transaction_service: AbsFinancialTransactionService = Depends(get_financial_transaction_service),
):
    try:
        result = await financial_transaction_service.delete_financial_transaction(pydantic_to_dto(FinancialTransactionDTO, financial_transaction))
        if not result:
            raise_404(data={"errors": "FinancialTransaction not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
