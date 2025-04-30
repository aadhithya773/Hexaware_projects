class Artwork:
    def __init__(self, title, description, creation_date, medium, image_url, artist_id,artwork_id=None):
        self.__artwork_id = artwork_id  # Primary key - No setter
        self.__title = title
        self.__description = description
        self.__creation_date = creation_date
        self.__medium = medium
        self.__image_url = image_url
        self.__artist_id = artist_id

    # Only Getter for artwork_id (No Setter)
    def get_artwork_id(self):
        return self.__artwork_id

    # Getter and Setter for title
    def get_title(self):
        return self.__title

    def set_title(self, title):
        if title:  # Basic validation
            self.__title = title
        else:
            raise ValueError("Title cannot be empty.")

    # Getter and Setter for description
    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    # Getter and Setter for creation_date
    def get_creation_date(self):
        return self.__creation_date

    def set_creation_date(self, creation_date):
        self.__creation_date = creation_date

    # Getter and Setter for medium
    def get_medium(self):
        return self.__medium

    def set_medium(self, medium):
        self.__medium = medium

    # Getter and Setter for image_url
    def get_image_url(self):
        return self.__image_url

    def set_image_url(self, image_url):
        self.__image_url = image_url

    # Getter and Setter for artist_id (Foreign Key)
    def get_artist_id(self):
        return self.__artist_id

    def set_artist_id(self, artist_id):
        self.__artist_id = artist_id
