import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.account import Account

class ZeroBalanceAccount(Account):
    def __init__(self, account_type="ZeroBalance", balance=0.0, customer=None):
        super().__init__(account_type, balance, customer)

    def withdraw(self, amount):
        if amount > self.account_balance:
            raise ValueError("Insufficient balance. ZeroBalanceAccount does not support overdraft.")
        self.account_balance -= amount
        return self.account_balance

    def calculate_interest(self):
        # Zero Balance accounts typically don't earn interest
        return 0.0

    def print_account_info(self):
        super().print_account_info()
        print("Note: This is a Zero Balance Account (No minimum balance required).")
