#task 8 
#from entity.account import Account

# class SavingsAccount(Account):
#     def __init__(self, account_number, account_type, interest_rate, balance=0):
#         super().__init__(account_number, account_type, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.account_balance * self.interest_rate / 100
#         self.account_balance += interest
#         print(f"Interest added: {interest}, New Balance: {self.account_balance}")

# Task 9: Inherit from BankAccount
import sys
import os
# import entity.bank_account
# print(dir(entity.bank_account))  # This should list BankAccount

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from entity.bank_account import BankAccount

# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, customer_name, balance=0.0, interest_rate=0.0):
#         super().__init__(account_number, customer_name, balance)
#         self.interest_rate = interest_rate

#     def deposit(self, amount: float):
#         self.balance += amount
#         print(f"Deposited {amount:.2f}. New Balance: {self.balance:.2f}")

#     def withdraw(self, amount: float):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount:.2f}. New Balance: {self.balance:.2f}")
#         else:
#             print("Insufficient balance.")

#     def calculate_interest(self):
#         interest = self.balance * (self.interest_rate / 100)
#         self.balance += interest
#         print(f"Interest of {interest:.2f} added. New Balance: {self.balance:.2f}")

from entity.account import Account
from exception.exceptions import InsufficientFundException

class SavingsAccount(Account):
    MINIMUM_BALANCE = 500.0

    def __init__(self, account_type="Savings", balance=500.0, customer=None, interest_rate=0.03):
        if balance < self.MINIMUM_BALANCE:
            raise ValueError(f"Savings Account requires a minimum balance of ₹{self.MINIMUM_BALANCE}")
        super().__init__(account_type, balance, customer)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.account_balance - amount < self.MINIMUM_BALANCE:
            raise InsufficientFundException("Cannot withdraw. Minimum balance requirement not met.")
        self.account_balance -= amount
        print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.account_balance}")
        return self.account_balance

    def calculate_interest(self):
        interest = self.account_balance * self.interest_rate
        self.account_balance += interest
        print(f"Interest of ₹{interest:.2f} added. New Balance: ₹{self.account_balance:.2f}")
        return interest

    # Optional: Print account info with interest rate
    def print_account_info(self):
        super().print_account_info()
        print(f"Interest Rate: {self.interest_rate * 100}%")
