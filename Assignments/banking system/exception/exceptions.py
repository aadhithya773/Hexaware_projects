# exception.py

class InsufficientFundException(Exception):
    def __init__(self, message="Insufficient funds in the account"):
        self.message = message
        super().__init__(self.message)

class InvalidAccountException(Exception):
    def __init__(self, message="Invalid account number"):
        self.message = message
        super().__init__(self.message)

class OverDraftLimitExceededException(Exception):
    def __init__(self, message="Overdraft limit exceeded in current account"):
        self.message = message
        super().__init__(self.message)

class NullPointerException(Exception):
    def __init__(self, message="Null value encountered"):
        self.message = message
        super().__init__(self.message)

class InvalidCustomerException(Exception):
    def __init__(self, message):
        super().__init__(message)

