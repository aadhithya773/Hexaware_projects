class Artist:
    def __init__(self,name, biography, birth_date, nationality, website, contact_info,artist_id=None):
        self.__artist_id = artist_id
        self.__name = name
        self.__biography = biography
        self.__birth_date = birth_date
        self.__nationality = nationality
        self.__website = website
        self.__contact_info = contact_info

    # Getter and setter for artist_id 
    def get_artist_id(self):
        return self.__artist_id


    # Getter and Setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name:
            self.__name = name
        else:
            raise ValueError("Name cannot be empty.")

    # Getter and Setter for biography
    def get_biography(self):
        return self.__biography

    def set_biography(self, biography):
        self.__biography = biography

    # Getter and Setter for birth_date
    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    # Getter and Setter for nationality
    def get_nationality(self):
        return self.__nationality

    def set_nationality(self, nationality):
        self.__nationality = nationality

    # Getter and Setter for website
    def get_website(self):
        return self.__website

    def set_website(self, website):
        self.__website = website

    # Getter and Setter for contact_info
    def get_contact_info(self):
        return self.__contact_info

    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info
