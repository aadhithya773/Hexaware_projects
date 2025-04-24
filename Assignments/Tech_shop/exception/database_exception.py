class DatabaseException(Exception):
    def __init__(self, message="Database access error."):
        super().__init__(message)
