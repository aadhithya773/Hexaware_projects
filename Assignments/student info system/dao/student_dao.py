# dao/student_dao.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from entity.student import Student
from util.db_conn_util import DBConnUtil
from exception.custom_exeption import StudentNotFoundException

class StudentDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()
    
    def get_all_students(self):
        students = []
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT student_id, first_name, last_name, date_of_birth, email, phone_number FROM students")
            rows = cursor.fetchall()
            for row in rows:
                print(f"Row fetched from DB: {row}")  # Debug
                print(f"Length: {len(row)}")   
                students.append(Student(*row))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
        return students

    def add_student(self, student: Student):
        try:
            query = """
            INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            self.cursor.execute(query, (
                student.student_id, student.first_name, student.last_name,
                student.date_of_birth, student.email, student.phone_number
            ))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def get_student_by_id(self, student_id):
        query = "SELECT * FROM Students WHERE student_id = ?"
        self.cursor.execute(query, (student_id,))
        row = self.cursor.fetchone()
        if row:
            return Student(*row)
        else:
            raise StudentNotFoundException(f"Student with ID {student_id} not found.")

    def update_student(self, student: Student):
        query = """
        UPDATE Students SET first_name = ?, last_name = ?, date_of_birth = ?, email = ?, phone_number = ?
        WHERE student_id = ?
        """
        self.cursor.execute(query, (
            student.first_name, student.last_name, student.date_of_birth,
            student.email, student.phone_number, student.student_id
        ))
        if self.cursor.rowcount == 0:
            raise StudentNotFoundException(f"Student with ID {student.student_id} not found.")
        self.conn.commit()

    def delete_student(self, student_id):
        query = "DELETE FROM Students WHERE student_id = ?"
        self.cursor.execute(query, (student_id,))
        if self.cursor.rowcount == 0:
            raise StudentNotFoundException(f"Student with ID {student_id} not found.")
        self.conn.commit()
