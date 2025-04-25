import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exception.Payment_failed_exception import PaymentFailedException
from datetime import datetime

class Order:
    def __init__(self, order_id, customer, order_date, total_amount):
        self._order_id = order_id
        self._customer = customer
        self._order_date = order_date
        self._total_amount = total_amount
        self._status = "Pending"
        self._order_details = []

    @property
    def order_id(self): 
        return self._order_id
    
    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    @property
    def customer(self): 
        return self._customer

    @customer.setter
    def customer(self, value):
        self._customer = value

    @property
    def order_date(self): 
        return self._order_date

    @order_date.setter
    def order_date(self, value):
        self._order_date = value

    @property
    def total_amount(self): 
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    @property
    def status(self): 
        return self._status

    @status.setter
    def status(self, value): 
        self._status = value

    def calculate_total_amount(self):
        self._total_amount = sum(od.calculate_subtotal() for od in self._order_details)
        return self._total_amount

    def get_order_details(self):
        details = f"Order {self._order_id} by {self._customer.first_name} on {self._order_date} - Status: {self._status}"
        for od in self._order_details:
            details += "\n" + od.get_order_detail_info()
        return details

    def update_order_status(self, new_status):
        self.status = new_status

    def cancel_order(self):
        self._status = "Cancelled"
    
    def process_payment(self, payment_info):
        success = False
        if not success:
            raise PaymentFailedException("Payment declined. Try again.")
