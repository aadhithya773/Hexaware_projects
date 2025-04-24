import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exception.incomplete_order import IncompleteOrderException

class OrderDetail:
    def __init__(self, order_detail_id, order, product, quantity):
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity = quantity
        self.__discount = 0

    @property
    def order(self): return self.__order

    @property
    def product(self): return self.__product

    @property
    def quantity(self): return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.__quantity = value

    def calculate_subtotal(self):
        return self.__product.price * self.__quantity * (1 - self.__discount / 100)

    def get_order_detail_info(self):
        return f"{self.__product.product_name} x {self.__quantity} = ₹{self.calculate_subtotal():.2f}"

    def update_quantity(self, qty):
        self.quantity = qty

    def add_discount(self, percent):
        self.__discount = percent
    
    # In OrderDetails class

    def validate(self):
        if self.__product is None or self.__order is None:
            raise IncompleteOrderException("OrderDetail missing product or order reference.")

