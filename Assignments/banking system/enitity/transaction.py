from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, amount, account_id, transaction_date=None, transaction_id=None):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.transaction_date = transaction_date if transaction_date else datetime.now()

    def print_transaction_info(self):
        print(f"\n--- Transaction Details ---")
        print(f"Transaction ID   : {self.transaction_id}")
        print(f"Account ID       : {self.account_id}")
        print(f"Type             : {self.transaction_type}")
        print(f"Amount           : ₹{self.amount:.2f}")
        print(f"Date             : {self.transaction_date}")
