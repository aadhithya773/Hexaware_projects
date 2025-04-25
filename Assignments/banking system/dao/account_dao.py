import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from dao.db_connection import get_connection
from dao.customer_dao import CustomerDAO
from entity.savings_account import SavingsAccount
from entity.current_account import CurrentAccount
from exception.exceptions import InvalidAccountException

class AccountDAO:
    def __init__(self):
        self.customer_dao = CustomerDAO()

    def insert_account(self, account):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO accounts (account_type, account_balance, customer_id)
                VALUES (?, ?, ?)
            """, (account.account_type, account.account_balance, account.customer.customer_id))
            conn.commit()
            print("Account inserted successfully.")
        except pyodbc.Error as e:
            print("Error while inserting account:", e)
        finally:
            conn.close()

    def get_account_by_id(self, account_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT account_number, account_type, account_balance, customer_id
                FROM accounts WHERE account_number = ?
            """, (account_id,))
            row = cursor.fetchone()
            if row:
                customer = self.customer_dao.get_customer_by_id(row.customer_id)
                if row.account_type == "Savings":
                    account = SavingsAccount(row.account_balance, customer)
                elif row.account_type == "Current":
                    account = CurrentAccount(row.account_balance, customer)
                else:
                    raise InvalidAccountException("Unknown account type.")
                account.account_number = row.account_number  # overwrite generated ID
                return account
            else:
                print(f"No account found with ID {account_id}")
        except pyodbc.Error as e:
            print("Error fetching account:", e)
        finally:
            conn.close()

    def get_accounts_by_customer(self, customer_id):
        conn = get_connection()
        accounts = []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT account_number, account_type, account_balance
                FROM accounts WHERE customer_id = ?
            """, (customer_id,))
            rows = cursor.fetchall()
            customer = self.customer_dao.get_customer_by_id(customer_id)
            for row in rows:
                if row.account_type == "Savings":
                    acc = SavingsAccount(row.account_balance, customer)
                elif row.account_type == "Current":
                    acc = CurrentAccount(row.account_balance, customer)
                else:
                    continue
                acc.account_number = row.account_number
                accounts.append(acc)
            return accounts
        except pyodbc.Error as e:
            print("Error fetching accounts:", e)
        finally:
            conn.close()

    def update_account(self, account):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE accounts SET account_balance = ?
                WHERE account_number = ?
            """, (account.account_balance, account.account_number))
            conn.commit()
            print("Account updated successfully.")
        except pyodbc.Error as e:
            print("Error updating account:", e)
        finally:
            conn.close()

    def delete_account(self, account_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM accounts WHERE account_number = ?", (account_id,))
            conn.commit()
            print("Account deleted successfully.")
        except pyodbc.Error as e:
            print("Error deleting account:", e)
        finally:
            conn.close()
