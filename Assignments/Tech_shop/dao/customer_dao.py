# dao/CustomerDAO.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.database_connector import DatabaseConnector
from entity.customer import Customer
from exception.database_exception import DatabaseException

class CustomerDAO:
    def __init__(self):
        self.db = DatabaseConnector()

    def list_customers(self):
        try:
            conn = self.db.open_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customers")
            rows = cursor.fetchall()
            customers = [Customer(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]
            return customers
        except Exception as e:
            raise DatabaseException(f"List customers failed: {e}")
        finally:
            self.db.close_connection()


    def create_customer(self, customer):
        try:
            conn = self.db.open_connection()  # fix here
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES (?, ?, ?, ?, ?)",
                (customer.first_name, customer.last_name, customer.email, customer.phone, customer.address)
            )
            conn.commit()
        except Exception as e:
            raise DatabaseException(f"Insert failed: {e}")
        finally:
            self.db.close_connection()


    def get_customer(self, customer_id):
        try:
            conn = self.db.open_connection()  # fix here
            cursor = conn.cursor()
            cursor.execute("SELECT CustomerID, FirstName, LastName, Email, Phone, Address FROM Customers WHERE CustomerID = ?", (customer_id,))
            row = cursor.fetchone()
            if row:
                return Customer(row[0], row[1], row[2], row[3], row[4], row[5])
            return None
        except Exception as e:
            raise DatabaseException(f"Get failed: {e}")
        finally:
            self.db.close_connection()


    def update_customer(self, customer):
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE Customers
                    SET FirstName = ?, LastName = ?, Email = ?, Phone = ?, Address = ?
                    WHERE CustomerID = ?
                """, (customer.first_name, customer.last_name, customer.email, customer.phone, customer.address, customer.customer_id))
                conn.commit()
        except Exception as e:
            raise DatabaseException(f"Update failed: {e}")

    def delete_customer(self, customer_id):
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Customers WHERE CustomerID = ?", (customer_id,))
                conn.commit()
        except Exception as e:
            raise DatabaseException(f"Delete failed: {e}")
