# dao/order_dao.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.database_connector import DatabaseConnector
from entity.order import Order
from exception.database_exception import DatabaseException
from dao.customer_dao import CustomerDAO

class OrderDAO:
    def __init__(self):
        self.db = DatabaseConnector()
        self.customer_dao = CustomerDAO()

    def create_order(self, order):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
                VALUES (?, ?, ?)
            """, (order.customer.customer_id, order.order_date, order.total_amount))
            conn.commit()
        except Exception as e:
            raise DatabaseException(f"Create order failed: {e}")
        finally:
            self.db.close_connection()

    def get_order(self, order_id):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Orders WHERE OrderID = ?", (order_id,))
            row = cursor.fetchone()
            if row:
                customer = self.customer_dao.get_customer(row[1])
                return Order(row[0], customer, row[2], row[3])
            return None
        except Exception as e:
            raise DatabaseException(f"Get order failed: {e}")
        finally:
            self.db.close_connection()

    def list_orders(self):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Orders")
            rows = cursor.fetchall()
            orders = []
            for row in rows:
                customer = self.customer_dao.get_customer(row[1])
                orders.append(Order(row[0], customer, row[2], row[3]))
            return orders
        except Exception as e:
            raise DatabaseException(f"List orders failed: {e}")
        finally:
            self.db.close_connection()

    def delete_order(self, order_id):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Orders WHERE OrderID = ?", (order_id,))
            conn.commit()
        except Exception as e:
            raise DatabaseException(f"Delete order failed: {e}")
        finally:
            self.db.close_connection()