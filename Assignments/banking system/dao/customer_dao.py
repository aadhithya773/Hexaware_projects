import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from util.db_util import DBUtil
from entity.customer import Customer
from exception.exceptions import InvalidCustomerException

class CustomerDAO:
    def __init__(self):
        self.connection = DBUtil.get_connection()

    def insert_customer(self, customer: Customer):
        try:
            cursor = self.connection.cursor()
            print("DOB Type:", type(customer.dob), "Value:", customer.dob)
            query = """
            INSERT INTO customers (first_name, last_name, dob, email, phone_number, address)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            params = (customer.first_name, customer.last_name, customer.dob, 
                      customer.email, customer.phone_number, customer.address)
            cursor.execute(query, params)
            self.connection.commit()
            print("Customer inserted successfully.")
        except Exception as e:
            print(f"Error while inserting customer: {e}")
            self.connection.rollback()
        finally:
            cursor.close()

    def update_customer(self, customer: Customer):
        try:
            cursor = self.connection.cursor()
            query = """
            UPDATE customers 
            SET first_name = ?, last_name = ?, dob = ?, email = ?, 
                phone_number = ?, address = ? 
            WHERE customer_id = ?
            """
            params = (customer.first_name, customer.last_name, customer.dob, 
                      customer.email, customer.phone_number, customer.address, customer.customer_id)
            cursor.execute(query, params)
            self.connection.commit()
            print("Customer updated successfully.")
        except Exception as e:
            print(f"Error while updating customer: {e}")
            self.connection.rollback()
        finally:
            cursor.close()

    def delete_customer(self, customer_id: int):
      def delete_customer(self, customer_id):
        try:
            cursor = self.conn.cursor()
            
            # Step 1: Get all account_ids for the customer
            cursor.execute("SELECT account_id FROM accounts WHERE customer_id = ?", (customer_id,))
            account_ids = [row[0] for row in cursor.fetchall()]

            # Step 2: Delete from transactions for those accounts
            for acc_id in account_ids:
                cursor.execute("DELETE FROM transactions WHERE account_id = ?", (acc_id,))

            # Step 3: Delete from accounts
            cursor.execute("DELETE FROM accounts WHERE customer_id = ?", (customer_id,))
            
            # Step 4: Delete from customers
            cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))

            self.conn.commit()
            print("Customer deleted successfully.")

        except pyodbc.Error as e:
            print("Error while deleting customer:", e)

        finally:
            cursor.close()

    def get_customer_by_id(self, customer_id: int):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM customers WHERE customer_id = ?"
            cursor.execute(query, (customer_id,))
            row = cursor.fetchone()
            if row:
                customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                return customer
            else:
                raise InvalidCustomerException(f"Customer with ID {customer_id} not found.")
        except InvalidCustomerException as e:
            print(e)
        except Exception as e:
            print(f"Error while fetching customer: {e}")
        finally:
            cursor.close()

    def get_customer_by_email(self, email: str):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM customers WHERE email = ?"
            cursor.execute(query, (email,))
            row = cursor.fetchone()
            if row:
                customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                return customer
            else:
                raise InvalidCustomerException(f"Customer with email {email} not found.")
        except InvalidCustomerException as e:
            print(e)
        except Exception as e:
            print(f"Error while fetching customer by email: {e}")
        finally:
            cursor.close()

