from abc import ABC, abstractmethod

class ICustomerServiceProvider(ABC):

    @abstractmethod
    def get_account_balance(self, account_number: int) -> float:
        """Retrieve the balance of the account with the given account number."""
        pass

    @abstractmethod
    def deposit(self, account_number: int, amount: float) -> float:
        """Deposit the specified amount into the account."""
        pass

    @abstractmethod
    def withdraw(self, account_number: int, amount: float) -> float:
        """Withdraw the specified amount from the account."""
        pass

    @abstractmethod
    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        """Transfer the specified amount from one account to another."""
        pass

    @abstractmethod
    def get_account_details(self, account_number: int) -> dict:
        """Return full account and customer details for the given account number."""
        pass
