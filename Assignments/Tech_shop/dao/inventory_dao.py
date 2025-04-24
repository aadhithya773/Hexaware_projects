# dao/inventory_dao.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.database_connector import DatabaseConnector
from entity.inventory import Inventory
from exception.database_exception import DatabaseException
from dao.product_dao import ProductDAO

class InventoryDAO:
    def __init__(self):
        self.db = DatabaseConnector()
        self.product_dao = ProductDAO()

    def update_inventory(self, product_id, quantity):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Inventory SET QuantityInStock = ? WHERE ProductID = ?",
                (quantity, product_id)
            )
            conn.commit()
        except Exception as e:
            raise DatabaseException(f"Update inventory failed: {e}")
        finally:
            self.db.close_connection()

    def get_inventory(self, product_id):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Inventory WHERE ProductID = ?", (product_id,))
            row = cursor.fetchone()
            if row:
                return Inventory(row[0], row[1])
            return None
        except Exception as e:
            raise DatabaseException(f"Get inventory failed: {e}")
        finally:
            self.db.close_connection()

    def list_inventory(self):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT InventoryID, ProductID, QuantityInStock FROM Inventory")
            rows = cursor.fetchall()
            inventory_list = []
            for row in rows:
                product = self.product_dao.get_product(row[1])
                inventory_list.append(Inventory(row[0], product, row[2]))
            return inventory_list
        except Exception as e:
            raise DatabaseException(f"List inventory failed: {e}")
        finally:
            self.db.close_connection()
