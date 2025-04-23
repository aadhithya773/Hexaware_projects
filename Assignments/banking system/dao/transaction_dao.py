import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from dao.db_connection import get_connection
from entity.transaction import Transaction

class TransactionDAO:

    def insert_transaction(self, transaction: Transaction):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO transactions (account_id, transaction_type, amount, transaction_date)
                VALUES (?, ?, ?, ?)
            """, (transaction.account_id, transaction.transaction_type, transaction.amount, transaction.transaction_date))
            conn.commit()
            print("Transaction inserted successfully.")
        except pyodbc.Error as e:
            print("Error inserting transaction:", e)
        finally:
            conn.close()

    def get_transaction_by_id(self, transaction_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT transaction_id, account_id, transaction_type, amount, transaction_date
                FROM transactions WHERE transaction_id = ?
            """, (transaction_id,))
            row = cursor.fetchone()
            if row:
                return Transaction(
                    transaction_type=row.transaction_type,
                    amount=row.amount,
                    account_id=row.account_id,
                    transaction_date=row.transaction_date,
                    transaction_id=row.transaction_id
                )
            else:
                print(f"No transaction found with ID {transaction_id}")
        except pyodbc.Error as e:
            print("Error fetching transaction:", e)
        finally:
            conn.close()

    def get_transactions_by_account(self, account_id):
        conn = get_connection()
        transactions = []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT transaction_id, account_id, transaction_type, amount, transaction_date
                FROM transactions WHERE account_id = ?
                ORDER BY transaction_date DESC
            """, (account_id,))
            rows = cursor.fetchall()
            for row in rows:
                txn = Transaction(
                    transaction_type=row.transaction_type,
                    amount=row.amount,
                    account_id=row.account_id,
                    transaction_date=row.transaction_date,
                    transaction_id=row.transaction_id
                )
                transactions.append(txn)
            return transactions
        except pyodbc.Error as e:
            print("Error fetching transactions:", e)
        finally:
            conn.close()

    def delete_transaction(self, transaction_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM transactions WHERE transaction_id = ?", (transaction_id,))
            conn.commit()
            print("Transaction deleted successfully.")
        except pyodbc.Error as e:
            print("Error deleting transaction:", e)
        finally:
            conn.close()
    
    def update_transaction(self, transaction: Transaction):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE transactions
                SET transaction_type = ?, amount = ?, transaction_date = ?
                WHERE transaction_id = ?
            """, (transaction.transaction_type, transaction.amount, transaction.transaction_date, transaction.transaction_id))
            conn.commit()
            print("Transaction updated successfully.")
        except pyodbc.Error as e:
            print("Error updating transaction:", e)
        finally:
            conn.close()
    
    def transfer_funds(self, from_account_id, to_account_id, amount):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            # Start a transaction
            conn.autocommit = False

            # 1. Check balance of from_account
            cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (from_account_id,))
            row = cursor.fetchone()
            if not row:
                raise Exception("Source account not found")
            if row.balance < amount:
                raise Exception("Insufficient balance in source account")

            # 2. Debit from source account
            cursor.execute("""
                UPDATE accounts SET balance = balance - ? WHERE account_id = ?
            """, (amount, from_account_id))

            cursor.execute("""
                INSERT INTO transactions (account_id, transaction_type, amount, transaction_date)
                VALUES (?, 'transfer', ?, GETDATE())
            """, (from_account_id, amount))

            # 3. Credit to destination account
            cursor.execute("""
                UPDATE accounts SET balance = balance + ? WHERE account_id = ?
            """, (amount, to_account_id))

            cursor.execute("""
                INSERT INTO transactions (account_id, transaction_type, amount, transaction_date)
                VALUES (?, 'deposit', ?, GETDATE())
            """, (to_account_id, amount))

            # 4. Commit transaction
            conn.commit()
            print("Transfer completed successfully.")
        except Exception as e:
            conn.rollback()
            print("Transfer failed:", e)
        finally:
            conn.close()


