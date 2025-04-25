# dao/enrollment_dao.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from entity.enrollment import Enrollment
from util.db_conn_util import DBConnUtil
from exception.custom_exeption import InvalidEnrollmentDataException

class EnrollmentDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()
    
    def get_all_enrollments(self):
        enrollments = []
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT enrollment_id, student_id, course_id, enrollment_date FROM Enrollments")
            rows = cursor.fetchall()
            for row in rows:
                enrollments.append(Enrollment(*row))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
        return enrollments

    def add_enrollment(self, enrollment: Enrollment):
        try:
            query = """
            INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date)
            VALUES (?, ?, ?, ?)
            """
            self.cursor.execute(query, (
                enrollment.enrollment_id,
                enrollment.student_id,
                enrollment.course_id,
                enrollment.enrollment_date
            ))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise InvalidEnrollmentDataException(f"Failed to add enrollment: {e}")

    def get_enrollment_by_id(self, enrollment_id):
        query = "SELECT * FROM Enrollments WHERE enrollment_id = ?"
        self.cursor.execute(query, (enrollment_id,))
        row = self.cursor.fetchone()
        if row:
            return Enrollment(*row)
        else:
            raise InvalidEnrollmentDataException(f"Enrollment with ID {enrollment_id} not found.")

    def update_enrollment(self, enrollment: Enrollment):
        query = """
        UPDATE Enrollments SET student_id = ?, course_id = ?, enrollment_date = ?
        WHERE enrollment_id = ?
        """
        self.cursor.execute(query, (
            enrollment.student_id,
            enrollment.course_id,
            enrollment.enrollment_date,
            enrollment.enrollment_id
        ))
        if self.cursor.rowcount == 0:
            raise InvalidEnrollmentDataException(f"Enrollment with ID {enrollment.enrollment_id} not found.")
        self.conn.commit()

    def delete_enrollment(self, enrollment_id):
        query = "DELETE FROM Enrollments WHERE enrollment_id = ?"
        self.cursor.execute(query, (enrollment_id,))
        if self.cursor.rowcount == 0:
            raise InvalidEnrollmentDataException(f"Enrollment with ID {enrollment_id} not found.")
        self.conn.commit()
