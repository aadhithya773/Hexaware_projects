class IncompleteOrderException(Exception):
    def __init__(self, message="Order is incomplete. Missing product reference."):
        super().__init__(message)
