''' TASK 8
class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone=None, address=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    # Getter and Setter Methods
    def get_customer_id(self):
        return self.customer_id
    
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email
    
    def get_phone(self):
        return self.phone
    
    def set_phone(self, phone):
        self.phone = phone
    
    def get_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address

    # Print All Information
    def print_customer_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")'''

# Task 10: Customer class with validation
import re

class Customer:
    def __init__(self, customer_id=None, first_name="", last_name="", dob="", email="", phone_number="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email  # Changed from email_address to email to match the test case
        self.phone_number = phone_number
        self.address = address

    # Getters
    def get_customer_id(self):
        return self.customer_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email  # Changed from get_email_address to get_email

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    # Setters
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        if self.is_valid_email(email):
            self.email = email
        else:
            raise ValueError("Invalid email address format")

    def set_phone_number(self, phone_number):
        if self.is_valid_phone(phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError("Phone number must be 10 digits")

    def set_address(self, address):
        self.address = address

    # Validators
    def is_valid_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def is_valid_phone(self, phone_number):
        return re.match(r"^\d{10}$", phone_number)

    # Method to print all details
    def print_customer_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of Birth: {self.dob}")  # Added dob here
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone_number}")
        print(f"Address: {self.address}")



