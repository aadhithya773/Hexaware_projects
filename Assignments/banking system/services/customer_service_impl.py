import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from service.i_customer_service import ICustomerServiceProvider
from entity.account import Account

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = []  # List to hold all accounts

    def get_account_by_number(self, account_number: int):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def get_account_balance(self, account_number: int):
        account = self.get_account_by_number(account_number)
        if account:
            return account.get_account_balance()
        else:
            raise ValueError("Account not found.")

    def deposit(self, account_number: int, amount: float):
        account = self.get_account_by_number(account_number)
        if account:
            account.set_account_balance(account.get_account_balance() + amount)
            return account.get_account_balance()
        else:
            raise ValueError("Account not found.")

    def withdraw(self, account_number: int, amount: float):
        account = self.get_account_by_number(account_number)
        if account:
            try:
                new_balance = account.withdraw(amount)
                return new_balance
            except ValueError as e:
                raise e
        else:
            raise ValueError("Account not found.")

    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        from_account = self.get_account_by_number(from_account_number)
        to_account = self.get_account_by_number(to_account_number)

        if from_account and to_account:
            try:
                self.withdraw(from_account_number, amount)
                self.deposit(to_account_number, amount)
            except ValueError as e:
                raise e
        else:
            raise ValueError("One or both account numbers not found.")

    def get_account_details(self, account_number: int):
        account = self.get_account_by_number(account_number)
        if account:
            account.print_account_info()
        else:
            raise ValueError("Account not found.")
