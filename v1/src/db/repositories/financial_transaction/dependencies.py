from v1.src.db.repositories.financial_transaction.repo import FinancialTransactionRepo
from v1.src.db.repositories.financial_transaction.abs_repo import AbsFinancialTransactionRepo


async def get_financial_transaction_repo() -> AbsFinancialTransactionRepo:
    return FinancialTransactionRepo()
