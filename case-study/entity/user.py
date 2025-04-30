class UserAccount:
    def __init__(self,  username, password, email, first_name, last_name, date_of_birth, profile_picture,user_id=None):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__email = email
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__profile_picture = profile_picture

    # Getter for user_id (No setter)
    def get_user_id(self):
        return self.__user_id

    # Getter and Setter for username
    def get_username(self):
        return self.__username

    def set_username(self, username):
        if username:
            self.__username = username
        else:
            raise ValueError("Username cannot be empty.")

    # Getter and Setter for password
    def get_password(self):
        return self.__password

    def set_password(self, password):
        if password:
            self.__password = password
        else:
            raise ValueError("Password cannot be empty.")

    # Getter and Setter for email
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    # Getter and Setter for first_name
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    # Getter and Setter for last_name
    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    # Getter and Setter for date_of_birth
    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    # Getter and Setter for profile_picture
    def get_profile_picture(self):
        return self.__profile_picture

    def set_profile_picture(self, profile_picture):
        self.__profile_picture = profile_picture
