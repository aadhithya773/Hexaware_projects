# dao/payment_dao.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from entity.payment import Payment
from util.db_conn_util import DBConnUtil
from exception.custom_exeption import PaymentValidationException

class PaymentDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()
    
    def get_all_payments(self):
        payments = []
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT payment_id, student_id, amount, payment_date FROM Payments")
            rows = cursor.fetchall()
            for row in rows:
                payments.append(Payment(*row))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
        return payments


    def add_payment(self, payment: Payment):
        try:
            query = """
            INSERT INTO Payments (payment_id, student_id, amount, payment_date)
            VALUES (?, ?, ?, ?)
            """
            self.cursor.execute(query, (
                payment.payment_id,
                payment.student_id,
                payment.amount,
                payment.payment_date
            ))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise PaymentValidationException(f"Failed to add payment: {e}")

    def get_payment_by_id(self, payment_id):
        query = "SELECT * FROM Payments WHERE payment_id = ?"
        self.cursor.execute(query, (payment_id,))
        row = self.cursor.fetchone()
        if row:
            return Payment(*row)
        else:
            raise PaymentValidationException(f"Payment with ID {payment_id} not found.")

    def update_payment(self, payment: Payment):
        query = """
        UPDATE Payments SET student_id = ?, amount = ?, payment_date = ?
        WHERE payment_id = ?
        """
        self.cursor.execute(query, (
            payment.student_id,
            payment.amount,
            payment.payment_date,
            payment.payment_id
        ))
        if self.cursor.rowcount == 0:
            raise PaymentValidationException(f"Payment with ID {payment.payment_id} not found.")
        self.conn.commit()

    def delete_payment(self, payment_id):
        query = "DELETE FROM Payments WHERE payment_id = ?"
        self.cursor.execute(query, (payment_id,))
        if self.cursor.rowcount == 0:
            raise PaymentValidationException(f"Payment with ID {payment_id} not found.")
        self.conn.commit()
