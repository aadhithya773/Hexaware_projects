import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.account import Account

class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store account_number: Account object

    def create_account(self, customer, account_type, balance):
        account = Account(account_type, balance, customer)
        self.accounts[account.account_number] = account
        print(f"\n✅ Account created successfully! Account Number: {account.account_number}")
        return account.account_number

    def get_account_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.get_account_balance()
        else:
            print("❌ Account not found.")
            return None

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            current_balance = account.get_account_balance() + amount
            account.set_account_balance(current_balance)
            print(f"✅ Amount {amount} deposited successfully. New Balance: {current_balance}")
            return current_balance
        else:
            print("❌ Account not found.")
            return None

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if account.get_account_balance() >= amount:
                new_balance = account.get_account_balance() - amount
                account.set_account_balance(new_balance)
                print(f"✅ Amount {amount} withdrawn successfully. New Balance: {new_balance}")
                return new_balance
            else:
                print("❌ Insufficient balance.")
        else:
            print("❌ Account not found.")
        return None

    def transfer(self, from_acc_no, to_acc_no, amount):
        from_account = self.accounts.get(from_acc_no)
        to_account = self.accounts.get(to_acc_no)

        if not from_account:
            print("❌ From Account not found.")
            return
        if not to_account:
            print("❌ To Account not found.")
            return
        if from_account.get_account_balance() < amount:
            print("❌ Insufficient balance in source account.")
            return

        # Perform transfer
        from_account.set_account_balance(from_account.get_account_balance() - amount)
        to_account.set_account_balance(to_account.get_account_balance() + amount)
        print(f"✅ Transfer successful! ₹{amount} transferred from {from_acc_no} to {to_acc_no}.")

    def get_account_details(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.print_account_info()
        else:
            print("❌ Account not found.")
