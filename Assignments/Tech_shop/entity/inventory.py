import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exception.Invalid_data_exception import InvalidDataException
from datetime import datetime
from exception.insufficient_stock_exception import InsufficientStockException
class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock):
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock
        self.__last_stock_update = datetime.now()

    def get_product(self): return self.__product

    def get_quantity_in_stock(self): return self.__quantity_in_stock

    def add_to_inventory(self, quantity):
        self.__quantity_in_stock += quantity
        self.__last_stock_update = datetime.now()

    def remove_from_inventory(self, quantity):
        if quantity > self.__quantity_in_stock:
            raise InsufficientStockException(f"Only {self.__quantity_in_stock} in stock.")
        self.__quantity_in_stock -= quantity    

    def update_stock_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.__quantity_in_stock = new_quantity
        self.__last_stock_update = datetime.now()

    def is_product_available(self, quantity):
        return self.__quantity_in_stock >= quantity

    def get_inventory_value(self):
        return self.__product.price * self.__quantity_in_stock

    def list_low_stock_products(self, threshold):
        return self.__product if self.__quantity_in_stock < threshold else None

    def list_out_of_stock_products(self):
        return self.__product if self.__quantity_in_stock == 0 else None

    def list_all_products(self):
        return f"{self.__product.product_name} - Stock: {self.__quantity_in_stock}"
