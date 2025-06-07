from abc import ABC, abstractmethod

from v1.src.app.dto.financial_transaction import FinancialTransactionDTO


class AbsFinancialTransactionService(ABC):
    @abstractmethod
    async def create_financial_transaction(self, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        pass

    @abstractmethod
    async def get_financial_transaction(self, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        pass

    @abstractmethod
    async def update_financial_transaction(self, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_financial_transaction(self, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        pass
