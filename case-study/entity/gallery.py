class Gallery:
    def __init__(self, name, description, location, curator_id, opening_hours,gallery_id=None):
        self.__gallery_id = gallery_id
        self.__name = name
        self.__description = description
        self.__location = location
        self.__curator_id = curator_id
        self.__opening_hours = opening_hours

    # Getter for gallery_id (No setter)
    def get_gallery_id(self):
        return self.__gallery_id
    def set_gallery_id(self, gallery_id):
        self.__gallery_id = gallery_id

    # Getter and Setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name:
            self.__name = name
        else:
            raise ValueError("Gallery name cannot be empty.")

    # Getter and Setter for description
    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    # Getter and Setter for location
    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    # Getter and Setter for curator_id
    def get_curator_id(self):
        return self.__curator_id

    def set_curator_id(self, curator_id):
        self.__curator_id = curator_id

    # Getter and Setter for opening_hours
    def get_opening_hours(self):
        return self.__opening_hours

    def set_opening_hours(self, opening_hours):
        self.__opening_hours = opening_hours
