''' TASK 8
from entity.account import Account

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000  # Overdraft limit for current account

    def __init__(self, account_number, account_type, balance=0):
        super().__init__(account_number, account_type, balance)

    def withdraw(self, amount):
        if isinstance(amount, (int, float)):
            if self.account_balance + CurrentAccount.OVERDRAFT_LIMIT >= amount:
                self.account_balance -= amount
                print(f"Withdrawn: {amount}, New Balance: {self.account_balance}")
            else:
                print(f"Insufficient funds. Overdraft limit exceeded. Current overdraft limit: {CurrentAccount.OVERDRAFT_LIMIT}")
        else:
            print("Invalid withdrawal amount")'''

# Task 9: Inherit from BankAccount
# from entity.bank_account import BankAccount

# class CurrentAccount(BankAccount):
#     OVERDRAFT_LIMIT = 5000  # Task 9: Constant overdraft limit

#     def __init__(self, account_number, customer_name, balance=0.0):
#         super().__init__(account_number, customer_name, balance)

#     def deposit(self, amount: float):
#         self.balance += amount
#         print(f"Deposited {amount:.2f}. New Balance: {self.balance:.2f}")

#     def withdraw(self, amount: float):
#         if self.balance - amount >= -CurrentAccount.OVERDRAFT_LIMIT:
#             self.balance -= amount
#             print(f"Withdrew {amount:.2f}. New Balance: {self.balance:.2f}")
#         else:
#             print("Withdrawal exceeds overdraft limit.")

#     def calculate_interest(self):
#         print("No interest is calculated for Current Accounts.")

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.account import Account
from exception.exceptions import InsufficientFundException, OverDraftLimitExceededException


class CurrentAccount(Account):
    OVERDRAFT_LIMIT = -10000.0  # You can go up to ₹10,000 in negative

    def __init__(self, account_type="Current", balance=0.0, customer=None):
        super().__init__(account_type, balance, customer)

    def withdraw(self, amount):
        if self.account_balance - amount < self.OVERDRAFT_LIMIT:
            raise OverDraftLimitExceededException("Withdrawal exceeds the overdraft limit.")
        self.account_balance -= amount
        return self.account_balance

    def calculate_interest(self):
        # Current accounts usually do not earn interest
        return 0.0

    def print_account_info(self):
        super().print_account_info()
        print(f"Overdraft Limit: ₹{abs(self.OVERDRAFT_LIMIT)}")
