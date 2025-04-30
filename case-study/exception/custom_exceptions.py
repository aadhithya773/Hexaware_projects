# exception/custom_exceptions.py

class ArtistNotFoundException(Exception):
    def __init__(self, message="Artist not found."):
        super().__init__(message)

class UserNotFoundException(Exception):
    def __init__(self, message="User not found."):
        super().__init__(message)

class ArtworkNotFoundException(Exception):
    def __init__(self, message="Artwork not found."):
        super().__init__(message)

class GalleryNotFoundException(Exception):
    def __init__(self, message="Gallery not found."):
        super().__init__(message)

class DuplicateFavoriteException(Exception):
    def __init__(self, message="Artwork already favorited by user."):
        super().__init__(message)

class DatabaseConnectionException(Exception):
    def __init__(self, message="Failed to connect to database."):
        super().__init__(message)

class InvalidDataException(Exception):
    def __init__(self, message="Invalid data entered."):
        super().__init__(message)

class DataNotFoundException(Exception):
    def __init__(self, message="No data found."):
        super().__init__(message)
