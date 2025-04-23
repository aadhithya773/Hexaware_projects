# Task 9: Abstract Base Class
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number=0, customer_name="", balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    # Getter and Setter Methods (Task 9)
    def get_account_number(self):
        return self.account_number

    def set_account_number(self, number):
        self.account_number = number

    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, name):
        self.customer_name = name

    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        self.balance = amount

    def print_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: {self.balance:.2f}")

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
