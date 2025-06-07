from fastapi import Depends

from v1.src.app.services.financial_transaction import build_financial_transaction_service, AbsFinancialTransactionService

async def get_financial_transaction_service(
    financial_transaction_service: AbsFinancialTransactionService = Depends(build_financial_transaction_service)
) -> AbsFinancialTransactionService:
    return financial_transaction_service
