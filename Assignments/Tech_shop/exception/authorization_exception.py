class AuthorizationException(Exception):
    def __init__(self, message="You are not authorized to perform this action."):
        super().__init__(message)
