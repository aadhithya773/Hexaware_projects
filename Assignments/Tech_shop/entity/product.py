import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exception.Invalid_data_exception import InvalidDataException
class Product:
    def __init__(self, product_id, product_name, description, price):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price

    @property
    def product_id(self): return self.__product_id

    @property
    def product_name(self): return self.__product_name

    @property
    def description(self): return self.__description

    @property
    def price(self): return self.__price

    @product_name.setter
    def product_name(self, value): self.__product_name = value

    @description.setter
    def description(self, value): self.__description = value

    @price.setter
    def price(self, value):
        if value < 0:
           raise InvalidDataException("Price cannot be negative.")
        self.__price = value

    def get_product_details(self):
        return f"{self.__product_id}: {self.__product_name} - {self.__description} @ ₹{self.__price:.2f}"

    def update_product_info(self, price=None, description=None):
        if price is not None: self.price = price
        if description is not None: self.description = description
