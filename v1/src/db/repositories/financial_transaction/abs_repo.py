from abc import ABC, abstractmethod

from v1.src.app.dto.financial_transaction import FinancialTransactionDTO


class AbsFinancialTransactionRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_financial_transaction(cls, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        raise NotImplementedError("create_financial_transaction() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_financial_transaction(cls, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        raise NotImplementedError("get_financial_transaction() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_financial_transaction(cls, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        raise NotImplementedError("update_financial_transaction() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_financial_transaction(cls, data: FinancialTransactionDTO) -> FinancialTransactionDTO | None | Exception:
        raise NotImplementedError("delete_financial_transaction() must be implemented in subclass")
