from v1.src.app.services.financial_transaction.abs_service import AbsFinancialTransactionService
from v1.src.app.services.financial_transaction.service import FinancialTransactionService

from v1.src.db.repositories.financial_transaction.dependencies import get_financial_transaction_repo


async def build_financial_transaction_service() -> AbsFinancialTransactionService:
    financial_transaction_repo = await get_financial_transaction_repo()
    return FinancialTransactionService(financial_transaction_repo)
