import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from service.customer_service_impl import CustomerServiceProviderImpl
from service.i_bank_service import IBankServiceProvider
from entity.savings_account import SavingsAccount
from entity.current_account import CurrentAccount
from entity.zero_balance_account import ZeroBalanceAccount

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name, branch_address):
        super().__init__()
        self.branch_name = branch_name
        self.branch_address = branch_address
        self.account_list = []  # holds all created account objects

    def create_account(self, customer, acc_type, balance):
        acc_type = acc_type.lower()
        account = None

        if acc_type == "savings":
            account = SavingsAccount(customer=customer, balance=balance)
        elif acc_type == "current":
            # You can ask for overdraft limit externally; hardcoded here for demo
            account = CurrentAccount(customer=customer, balance=balance, overdraft_limit=1000)
        elif acc_type == "zero":
            account = ZeroBalanceAccount(customer=customer)
        else:
            raise ValueError("Invalid account type.")

        self.account_list.append(account)
        print(f"\nAccount created successfully! Account Number: {account.get_account_number()}")
        return account

    def list_accounts(self):
        if not self.account_list:
            print("\nNo accounts found.")
        else:
            for acc in self.account_list:
                acc.print_account_info()
                print("-" * 30)

    def calculate_interest(self):
        for account in self.account_list:
            if hasattr(account, "calculate_interest"):
                interest = account.calculate_interest()
                account.account_balance += interest
                print(f"Interest ₹{interest:.2f} added to Account {account.get_account_number()}")
