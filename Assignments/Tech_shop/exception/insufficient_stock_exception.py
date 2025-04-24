class InsufficientStockException(Exception):
    def __init__(self, message="Not enough stock available."):
        super().__init__(message)
