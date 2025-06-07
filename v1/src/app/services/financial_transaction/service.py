from v1.src.app.services.financial_transaction.abs_service import AbsFinancialTransactionService
from v1.src.db.repositories.financial_transaction import AbsFinancialTransactionRepo
from v1.src.app.dto.financial_transaction import FinancialTransactionDTO


class FinancialTransactionService(AbsFinancialTransactionService):
    def __init__(self, financial_transaction_repo: AbsFinancialTransactionRepo):
        self.financial_transaction_repo = financial_transaction_repo

    async def create_financial_transaction(self, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        return await self.financial_transaction_repo.create_financial_transaction(data)

    async def get_financial_transaction(self, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        result = await self.financial_transaction_repo.get_financial_transaction(data)
        if not result:
            raise ValueError("Financial transaction not found")
        return result

    async def update_financial_transaction(self, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        result = await self.financial_transaction_repo.update_financial_transaction(data)
        if not result:
            raise ValueError("Cannot update: financial transaction not found")
        return result

    async def delete_financial_transaction(self, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        result = await self.financial_transaction_repo.delete_financial_transaction(data)
        if not result:
            raise ValueError("Cannot delete: financial transaction not found")
        return result
