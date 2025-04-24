# dao/product_dao.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.database_connector import DatabaseConnector
from entity.product import Product
from exception.database_exception import DatabaseException

class ProductDAO:
    def __init__(self):
        self.db = DatabaseConnector()

    def list_products(self):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products")
            rows = cursor.fetchall()
            products = [Product(row[0], row[1], row[2], row[3]) for row in rows]  # Index-based access
            return products
        except Exception as e:
            raise DatabaseException(f"List products failed: {e}")
        finally:
            self.db.close_connection()


    def create_product(self, product):
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO Products (ProductName, Description, Price)
                    VALUES (?, ?, ?)
                """, (product.product_name, product.description, product.price))
                conn.commit()
        except Exception as e:
            raise DatabaseException(f"Create product failed: {e}")

    def get_product(self, product_id):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products WHERE ProductID = ?", (product_id,))
            row = cursor.fetchone()
            if row:
                return Product(row[0], row[1], row[2], row[3])
            return None
        except Exception as e:
            raise DatabaseException(f"Get product failed: {e}")
        finally:
            self.db.close_connection()


    def update_product(self, product):
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE Products
                    SET ProductName = ?, Description = ?, Price = ?
                    WHERE ProductID = ?
                """, (product.product_name, product.description, product.price, product.product_id))
                conn.commit()
        except Exception as e:
            raise DatabaseException(f"Update product failed: {e}")

    def delete_product(self, product_id):
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Products WHERE ProductID = ?", (product_id,))
                conn.commit()
        except Exception as e:
            raise DatabaseException(f"Delete product failed: {e}")
