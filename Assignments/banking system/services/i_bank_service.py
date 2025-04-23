import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from abc import ABC, abstractmethod
from entity.customer import Customer

class IBankServiceProvider(ABC):

    @abstractmethod
    def create_account(self, customer: Customer, acc_type: str, balance: float):
        """Create a new account for a given customer with initial balance."""
        pass

    @abstractmethod
    def list_accounts(self) -> list:
        """Return a list of all accounts in the bank."""
        pass

    @abstractmethod
    def calculate_interest(self):
        """Calculate interest for applicable accounts."""
        pass
