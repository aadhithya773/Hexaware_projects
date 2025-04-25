# dao/order_detail_dao.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.database_connector import DatabaseConnector
from entity.order_detail import OrderDetail
from exception.database_exception import DatabaseException
from dao.order_dao import OrderDAO
from dao.product_dao import ProductDAO

class OrderDetailDAO:
    def __init__(self):
        self.db = DatabaseConnector()

    def create_order_detail(self, order_detail):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice) VALUES (?, ?, ?, ?)",
                (order_detail.order_id, order_detail.product_id, order_detail.quantity, order_detail.unit_price)
            )
            conn.commit()
        except Exception as e:
            raise DatabaseException(f"Create order detail failed: {e}")
        finally:
            self.db.close_connection()

    def get_order_details_by_order_id(self, order_id):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM OrderDetails WHERE OrderID = ?", (order_id,))
            rows = cursor.fetchall()
            return [OrderDetail(row[0], row[1], row[2], row[3]) for row in rows]
        except Exception as e:
            raise DatabaseException(f"Get order details failed: {e}")
        finally:
            self.db.close_connection()
