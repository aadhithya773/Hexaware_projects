# # entity/account.py
# class Account:
#     def __init__(self, account_number=None, account_type=None, account_balance=0.0):
#         self.account_number = account_number
#         self.account_type = account_type
#         self.account_balance = account_balance

#     # Getter and Setter Methods
#     def get_account_number(self):
#         return self.account_number
    
#     def set_account_number(self, account_number):
#         self.account_number = account_number
    
#     def get_account_type(self):
#         return self.account_type
    
#     def set_account_type(self, account_type):
#         self.account_type = account_type
    
#     def get_account_balance(self):
#         return self.account_balance
    
#     def set_account_balance(self, balance):
#         self.account_balance = balance
    
#     # Print All Information
#     def print_account_info(self):
#         print(f"Account Number: {self.account_number}")
#         print(f"Account Type: {self.account_type}")
#         print(f"Account Balance: {self.account_balance}")

#     # Deposit method - Overloaded for different data types
#     def deposit(self, amount):
#         if isinstance(amount, (int, float)):
#             if amount > 0:
#                 self.account_balance += amount
#                 print(f"Deposited: {amount}, New Balance: {self.account_balance}")
#             else:
#                 print("Invalid deposit amount")
#         else:
#             print("Invalid amount type. Please enter an int or float.")

#     # Withdrawal method - Overloaded for different data types
#     def withdraw(self, amount):
#         if isinstance(amount, (int, float)):
#             if amount > 0:
#                 if self.account_balance >= amount:
#                     self.account_balance -= amount
#                     print(f"Withdrawn: {amount}, New Balance: {self.account_balance}")
#                 else:
#                     print("Insufficient funds")
#             else:
#                 print("Invalid withdrawal amount")
#         else:
#             print("Invalid amount type. Please enter an int or float.")

#     # Calculate Interest method (Fixed interest rate of 4.5%)
#     def calculate_interest(self):
#         interest = self.account_balance * 4.5 / 100
#         self.account_balance += interest
#         print(f"Interest added: {interest}, New Balance: {self.account_balance}")



# Task 10: Account class with Has-A relation to Customer
# import os
# print(os.getcwd())

# from entity.customer import Customer

# class Account(Customer):
#     account_counter = 1000  # For auto-incrementing account numbers

#     def __init__(self, account_type="", balance=0.0, customer=None):
#         Account.account_counter += 1
#         self.account_number = Account.account_counter
#         self.account_type = account_type
#         self.account_balance = balance
#         self.customer = customer  # Has-A relation

#     # Getters
#     def get_account_number(self):
#         return self.account_number

#     def get_account_type(self):
#         return self.account_type

#     def get_account_balance(self):
#         return self.account_balance

#     def get_customer(self):
#         return self.customer

#     # Setters
#     def set_account_type(self, account_type):
#         self.account_type = account_type

#     def set_account_balance(self, balance):
#         self.account_balance = balance

#     def set_customer(self, customer):
#         self.customer = customer

#     # Print account and customer info
#     def print_account_info(self):
#         print(f"\n--- Account Details ---")
#         print(f"Account Number: {self.account_number}")
#         print(f"Account Type: {self.account_type}")
#         print(f"Account Balance: {self.account_balance}")
#         print(f"\n--- Customer Details ---")
#         self.customer.print_customer_info()


# #Task 11: abstract method convertion
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from abc import ABC, abstractmethod
# from entity.customer import Customer
# from exception.exceptions import InsufficientFundException, InvalidAccountException, OverDraftLimitExceededException

# class Account(ABC):
#     last_account_number = 1000  # static variable for auto-incrementing

#     def __init__(self, account_type, balance, customer: Customer):
#         Account.last_account_number += 1
#         self.account_number = Account.last_account_number
#         self.account_type = account_type
#         self.account_balance = balance
#         self.customer = customer

#     def get_account_number(self):
#         return self.account_number

#     def get_account_type(self):
#         return self.account_type

#     def get_account_balance(self):
#         return self.account_balance

#     def get_customer(self):
#         return self.customer

#     def set_account_type(self, account_type):
#         self.account_type = account_type

#     def set_account_balance(self, balance):
#         self.account_balance = balance

#     def set_customer(self, customer):
#         self.customer = customer

#     def print_account_info(self):
#         print(f"\n--- Account Details ---")
#         print(f"Account Number: {self.account_number}")
#         print(f"Account Type: {self.account_type}")
#         print(f"Account Balance: {self.account_balance}")
#         print(f"\n--- Customer Details ---")
#         self.customer.print_customer_info()

#     @abstractmethod
#     def withdraw(self, amount):
#          pass

#     @abstractmethod
#     def calculate_interest(self):
#         pass  # To be implemented by SavingsAccount only (others may return 0)

#Task 12:exception Handling
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from abc import ABC, abstractmethod
from entity.customer import Customer
from exception.exceptions import (
    InsufficientFundException,
    InvalidAccountException,
    OverDraftLimitExceededException
)

class Account(ABC):
    last_account_number = 1000  # static variable for auto-incrementing

    def __init__(self, account_type, balance, customer: Customer):
        if customer is None:
            raise TypeError("Customer cannot be None")  # acts like NullPointerException in Python
        Account.last_account_number += 1
        self.account_number = Account.last_account_number
        self.account_type = account_type
        self.account_balance = balance
        self.customer = customer

    def get_account_number(self):
        return self.account_number

    def get_account_type(self):
        return self.account_type

    def get_account_balance(self):
        return self.account_balance

    def get_customer(self):
        return self.customer

    def set_account_type(self, account_type):
        self.account_type = account_type

    def set_account_balance(self, balance):
        self.account_balance = balance

    def set_customer(self, customer):
        self.customer = customer

    def print_account_info(self):
        print(f"\n--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Balance: {self.account_balance}")
        print(f"\n--- Customer Details ---")
        self.customer.print_customer_info()

    def transfer(self, to_account, amount):
        if to_account is None:
            raise InvalidAccountException("Invalid target account.")
        if amount > self.account_balance:
            raise InsufficientFundException("Insufficient funds to complete transfer.")
        self.account_balance -= amount
        to_account.account_balance += amount
        print(f"Transferred ₹{amount:.2f} to Account {to_account.account_number}")
        return self.account_balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass  # To be implemented by subclasses

