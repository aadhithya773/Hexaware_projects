class ConcurrencyException(Exception):
    def __init__(self, message="Concurrent update error. Please try again."):
        super().__init__(message)
