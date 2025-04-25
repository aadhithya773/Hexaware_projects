import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.customer import Customer
from entity.savings_account import SavingsAccount
from entity.current_account import CurrentAccount
from entity.bank_account import BankAccount
#TASK 8
# class Bank:
#     def __init__(self):
#         self.accounts = []

#     # Create an Account
#     def create_account(self):
#         print("Select Account Type: ")
#         print("1. Savings Account")
#         print("2. Current Account")
#         choice = int(input("Enter your choice (1/2): "))
        
#         account_number = int(input("Enter Account Number: "))
#         account_type = "Savings" if choice == 1 else "Current"

#         if choice == 1:
#             interest_rate = float(input("Enter interest rate: "))
#             account = SavingsAccount(account_number, account_type, interest_rate=interest_rate)
#         elif choice == 2:
#             account = CurrentAccount(account_number, account_type)
#         else:
#             print("Invalid choice.")
#             return
        
#         self.accounts.append(account)
#         print(f"Account {account_number} created successfully.")

#     # Perform Deposit
#     def deposit(self):
#         account_number = int(input("Enter Account Number to Deposit: "))
#         amount = float(input("Enter Deposit Amount: "))
        
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 account.deposit(amount)
#                 break
#         else:
#             print("Account not found.")

#     # Perform Withdrawal
#     def withdraw(self):
#         account_number = int(input("Enter Account Number to Withdraw: "))
#         amount = float(input("Enter Withdraw Amount: "))
        
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 account.withdraw(amount)
#                 break
#         else:
#             print("Account not found.")

#     # Calculate and Add Interest
#     def calculate_interest(self):
#         account_number = int(input("Enter Account Number to Calculate Interest: "))
        
#         for account in self.accounts:
#             if account.account_number == account_number and isinstance(account, SavingsAccount):
#                 account.calculate_interest()
#                 break
#         else:
#             print("Account not found or not a Savings Account.")

# # Main method logic for execution
# if __name__ == "__main__":
#     # Creating Customer
#     customer1 = Customer(101, "John", "Doe", "john.doe@example.com", "1234567890", "1234 Elm Street")
#     customer1.print_customer_info()
    
#     # Creating Bank and Account
#     bank = Bank()
#     bank.create_account()
    
#     # Performing Deposit and Withdrawal
#     bank.deposit()
#     bank.withdraw()
    
#     # Calculate Interest on Savings Account
#     bank.calculate_interest()

#TASK 9: Updated for abstraction and polymorphism
'''class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        print("Select Account Type:")
        print("1. Savings Account")
        print("2. Current Account")
        choice = int(input("Enter choice (1 or 2): "))

        acc_no = int(input("Enter Account Number: "))
        name = input("Enter Customer Name: ")
        balance = float(input("Enter Initial Balance: "))

        if choice == 1:
            rate = float(input("Enter Interest Rate: "))
            account = SavingsAccount(acc_no, name, balance, rate)
        elif choice == 2:
            account = CurrentAccount(acc_no, name, balance)
        else:
            print("Invalid choice.")
            return

        self.accounts.append(account)
        print("Account created successfully.")

    def deposit(self):
        acc_no = int(input("Enter Account Number to Deposit: "))
        amount = float(input("Enter Amount to Deposit: "))

        for acc in self.accounts:
            if acc.account_number == acc_no:
                acc.deposit(amount)
                return
        print("Account not found.")

    def withdraw(self):
        acc_no = int(input("Enter Account Number to Withdraw: "))
        amount = float(input("Enter Amount to Withdraw: "))

        for acc in self.accounts:
            if acc.account_number == acc_no:
                acc.withdraw(amount)
                return
        print("Account not found.")

    def calculate_interest(self):
        acc_no = int(input("Enter Account Number to Calculate Interest: "))

        for acc in self.accounts:
            if acc.account_number == acc_no:
                acc.calculate_interest()
                return
        print("Account not found.")


if __name__ == "__main__":
    bank = Bank()
    while True:
        print("\n==== Banking Menu ====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Calculate Interest")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            bank.create_account()
        elif choice == 2:
            bank.deposit()
        elif choice == 3:
            bank.withdraw()
        elif choice == 4:
            bank.calculate_interest()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")'''

#task 11
# from exception.exceptions import InsufficientFundException, InvalidAccountException, OverDraftLimitExceededException
# from entity.savings_account import SavingsAccount
# from entity.current_account import CurrentAccount

# class Bank:
#     def __init__(self):
#         self.accounts = []

#     def create_account(self):
#         try:
#             print("Select Account Type:")
#             print("1. Savings Account")
#             print("2. Current Account")
#             choice = int(input("Enter choice (1 or 2): "))

#             acc_no = int(input("Enter Account Number: "))
#             name = input("Enter Customer Name: ")
#             balance = float(input("Enter Initial Balance: "))

#             if choice == 1:
#                 rate = float(input("Enter Interest Rate: "))
#                 account = SavingsAccount(acc_no, name, balance, rate)
#             elif choice == 2:
#                 account = CurrentAccount(acc_no, name, balance)
#             else:
#                 print("Invalid choice.")
#                 return

#             self.accounts.append(account)
#             print("Account created successfully.")

#         except Exception as e:
#             print(f"Error while creating account: {e}")

#     def deposit(self):
#         try:
#             acc_no = int(input("Enter Account Number to Deposit: "))
#             amount = float(input("Enter Amount to Deposit: "))

#             for acc in self.accounts:
#                 if acc.account_number == acc_no:
#                     acc.deposit(amount)
#                     print("Deposit successful.")
#                     return
#             raise InvalidAccountException("Account not found.")

#         except InvalidAccountException as e:
#             print(f"Error: {e}")
#         except Exception as e:
#             print(f"Unexpected Error: {e}")

#     def withdraw(self):
#         try:
#             acc_no = int(input("Enter Account Number to Withdraw: "))
#             amount = float(input("Enter Amount to Withdraw: "))

#             for acc in self.accounts:
#                 if acc.account_number == acc_no:
#                     acc.withdraw(amount)
#                     print("Withdrawal successful.")
#                     return
#             raise InvalidAccountException("Account not found.")

#         except InvalidAccountException as e:
#             print(f"Error: {e}")
#         except InsufficientFundException as e:
#             print(f"Error: {e}")
#         except OverDraftLimitExceededException as e:
#             print(f"Error: {e}")
#         except Exception as e:
#             print(f"Unexpected Error: {e}")

#     def calculate_interest(self):
#         try:
#             acc_no = int(input("Enter Account Number to Calculate Interest: "))

#             for acc in self.accounts:
#                 if acc.account_number == acc_no:
#                     acc.calculate_interest()
#                     return
#             raise InvalidAccountException("Account not found.")

#         except InvalidAccountException as e:
#             print(f"Error: {e}")
#         except Exception as e:
#             print(f"Unexpected Error: {e}")


# if __name__ == "__main__":
#     bank = Bank()
#     while True:
#         print("\n==== Banking Menu ====")
#         print("1. Create Account")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Calculate Interest")
#         print("5. Exit")
#         try:
#             choice = int(input("Enter your choice: "))

#             if choice == 1:
#                 bank.create_account()
#             elif choice == 2:
#                 bank.deposit()
#             elif choice == 3:
#                 bank.withdraw()
#             elif choice == 4:
#                 bank.calculate_interest()
#             elif choice == 5:
#                 print("Exiting...")
#                 break
#             else:
#                 print("Invalid choice.")
#         except ValueError:
#             print("Please enter a valid number.")


#Task 13(1):using list for storing accounts
# Task 13(1) - Using List for Accounts

# from exception.exceptions import InsufficientFundException, InvalidAccountException, OverDraftLimitExceededException
# from entity.savings_account import SavingsAccount
# from entity.current_account import CurrentAccount

# class Bank:
#     def __init__(self):
#         self.accounts = []  # List to store accounts

#     def create_account(self):
#         try:
#             print("Select Account Type:")
#             print("1. Savings Account")
#             print("2. Current Account")
#             choice = int(input("Enter choice (1 or 2): "))

#             acc_no = int(input("Enter Account Number: "))
#             name = input("Enter Customer Name: ")
#             balance = float(input("Enter Initial Balance: "))

#             if choice == 1:
#                 rate = float(input("Enter Interest Rate: "))
#                 account = SavingsAccount(acc_no, name, balance, rate)
#             elif choice == 2:
#                 account = CurrentAccount(acc_no, name, balance)
#             else:
#                 print("Invalid choice.")
#                 return

#             self.accounts.append(account)
#             print("Account created successfully.")

#         except Exception as e:
#             print(f"Error while creating account: {e}")

#     def deposit(self):
#         try:
#             acc_no = int(input("Enter Account Number to Deposit: "))
#             amount = float(input("Enter Amount to Deposit: "))

#             for acc in self.accounts:
#                 if acc.account_number == acc_no:
#                     acc.deposit(amount)
#                     print("Deposit successful.")
#                     return
#             raise InvalidAccountException("Account not found.")

#         except InvalidAccountException as e:
#             print(f"Error: {e}")
#         except Exception as e:
#             print(f"Unexpected Error: {e}")

#     def withdraw(self):
#         try:
#             acc_no = int(input("Enter Account Number to Withdraw: "))
#             amount = float(input("Enter Amount to Withdraw: "))

#             for acc in self.accounts:
#                 if acc.account_number == acc_no:
#                     acc.withdraw(amount)
#                     print("Withdrawal successful.")
#                     return
#             raise InvalidAccountException("Account not found.")

#         except InvalidAccountException as e:
#             print(f"Error: {e}")
#         except InsufficientFundException as e:
#             print(f"Error: {e}")
#         except OverDraftLimitExceededException as e:
#             print(f"Error: {e}")
#         except Exception as e:
#             print(f"Unexpected Error: {e}")

#     def calculate_interest(self):
#         try:
#             acc_no = int(input("Enter Account Number to Calculate Interest: "))

#             for acc in self.accounts:
#                 if acc.account_number == acc_no:
#                     acc.calculate_interest()
#                     return
#             raise InvalidAccountException("Account not found.")

#         except InvalidAccountException as e:
#             print(f"Error: {e}")
#         except Exception as e:
#             print(f"Unexpected Error: {e}")


# if __name__ == "__main__":
#     bank = Bank()
#     while True:
#         print("\n==== Banking Menu ====")
#         print("1. Create Account")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Calculate Interest")
#         print("5. Exit")
#         try:
#             choice = int(input("Enter your choice: "))

#             if choice == 1:
#                 bank.create_account()
#             elif choice == 2:
#                 bank.deposit()
#             elif choice == 3:
#                 bank.withdraw()
#             elif choice == 4:
#                 bank.calculate_interest()
#             elif choice == 5:
#                 print("Exiting...")
#                 break
#             else:
#                 print("Invalid choice.")
#         except ValueError:
#             print("Please enter a valid number.")



#Task 14 final main file for connecting with DAO
from dao.customer_dao import CustomerDAO
from dao.account_dao import AccountDAO
from dao.transaction_dao import TransactionDAO
from entity.customer import Customer
from entity.savings_account import SavingsAccount
from entity.current_account import CurrentAccount
from entity.transaction import Transaction
import datetime
def main():
    customer_dao = CustomerDAO()
    account_dao = AccountDAO()
    transaction_dao = TransactionDAO()

    while True:
        print("\n--- Banking System ---")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. View Transactions")
        print("7. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            create_customer(customer_dao)
        elif choice == "2":
            create_account(account_dao,customer_dao)
        elif choice == "3":
            deposit_money(account_dao, transaction_dao)
        elif choice == "4":
            withdraw_money(account_dao, transaction_dao)
        elif choice == "5":
            transfer_money(account_dao, transaction_dao)
        elif choice == "6":
            view_transactions(transaction_dao)
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

def create_customer(customer_dao):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter DOB in YYYY-MM-DD format.")
        return
    email = input("Enter email: ")
    phone_number = input("Enter phone number: ")
    address = input("Enter address: ")

    customer = Customer(first_name, last_name, dob, email, phone_number, address)
    customer_id = customer_dao.insert_customer(customer)

    if customer_id:
        print(f"Customer created successfully! Customer ID is: {customer_id}")
    else:
        print("Failed to create customer.")


def create_account(account_dao,customer_dao):
    customer_id = int(input("Enter customer ID: "))
    try:
        customer_id = int(input("Enter customer ID: "))
    except ValueError:
        print("Invalid input. Please enter a numeric customer ID.")
        return

    account_type = input("Enter account type (savings/current): ")
    balance = float(input("Enter initial balance: "))
    
    customer = customer_dao.get_customer_by_id(customer_id)
    if customer:
        if account_type == "savings":
            account = SavingsAccount(balance, customer)
        elif account_type == "current":
            account = CurrentAccount(balance, customer)
        else:
            print("Invalid account type!")
            return
        
        account_dao.insert_account(account)
        print(f"{account_type.capitalize()} account created successfully for customer {customer.first_name}!")

def deposit_money(account_dao, transaction_dao):
    account_id = int(input("Enter account ID to deposit into: "))
    amount = float(input("Enter amount to deposit: "))

    account = account_dao.get_account_by_id(account_id)
    if account:
        account.account_balance += amount
        account_dao.update_account(account)

        transaction = Transaction("deposit", amount, account_id)
        transaction_dao.insert_transaction(transaction)
        print(f"Deposited ₹{amount:.2f} into account {account_id}.")
    else:
        print("Account not found.")

def withdraw_money(account_dao, transaction_dao):
    account_id = int(input("Enter account ID to withdraw from: "))
    amount = float(input("Enter amount to withdraw: "))

    account = account_dao.get_account_by_id(account_id)
    if account:
        if account.account_balance >= amount:
            account.account_balance -= amount
            account_dao.update_account(account)

            transaction = Transaction("withdrawal", amount, account_id)
            transaction_dao.insert_transaction(transaction)
            print(f"Withdrew ₹{amount:.2f} from account {account_id}.")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found.")

def transfer_money(account_dao, transaction_dao):
    from_account_id = int(input("Enter source account ID: "))
    to_account_id = int(input("Enter destination account ID: "))
    amount = float(input("Enter amount to transfer: "))

    from_account = account_dao.get_account_by_id(from_account_id)
    to_account = account_dao.get_account_by_id(to_account_id)

    if from_account and to_account:
        if from_account.account_balance >= amount:
            # Deduct from source
            from_account.account_balance -= amount
            account_dao.update_account(from_account)

            # Add to destination
            to_account.account_balance += amount
            account_dao.update_account(to_account)

            # Record transactions
            transaction_dao.insert_transaction(Transaction("transfer", amount, from_account_id))
            transaction_dao.insert_transaction(Transaction("transfer", amount, to_account_id))
            print(f"Transferred ₹{amount:.2f} from account {from_account_id} to {to_account_id}.")
        else:
            print("Insufficient funds for transfer.")
    else:
        print("One or both accounts not found.")

def view_transactions(transaction_dao):
    account_id = int(input("Enter account ID to view transactions: "))
    transactions = transaction_dao.get_transactions_by_account(account_id)
    
    if transactions:
        for txn in transactions:
            txn.print_transaction_info()
    else:
        print("No transactions found for this account.")

if __name__ == "__main__":
    main()
