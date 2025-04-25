# dao/teacher_dao.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from entity.teacher import Teacher
from util.db_conn_util import DBConnUtil
from exception.custom_exeption import TeacherNotFoundException

class TeacherDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()
    
    def get_all_teachers(self):
        teachers = []
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT teacher_id, first_name, last_name, email FROM teacher")
            rows = cursor.fetchall()
            for row in rows:
                teachers.append(Teacher(*row))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
        return teachers


    def add_teacher(self, teacher: Teacher):
        try:
            query = """
            INSERT INTO Teacher (teacher_id, first_name, last_name, email)
            VALUES (?, ?, ?, ?)
            """
            self.cursor.execute(query, (
                teacher.teacher_id,
                teacher.first_name,
                teacher.last_name,
                teacher.email
            ))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def get_teacher_by_id(self, teacher_id):
        query = "SELECT * FROM Teacher WHERE teacher_id = ?"
        self.cursor.execute(query, (teacher_id,))
        row = self.cursor.fetchone()
        if row:
            return Teacher(*row)
        else:
            raise TeacherNotFoundException(f"Teacher with ID {teacher_id} not found.")

    def update_teacher(self, teacher: Teacher):
        query = """
        UPDATE Teacher SET first_name = ?, last_name = ?, email = ?
        WHERE teacher_id = ?
        """
        self.cursor.execute(query, (
            teacher.first_name,
            teacher.last_name,
            teacher.email,
            teacher.teacher_id
        ))
        if self.cursor.rowcount == 0:
            raise TeacherNotFoundException(f"Teacher with ID {teacher.teacher_id} not found.")
        self.conn.commit()

    def delete_teacher(self, teacher_id):
        query = "DELETE FROM Teacher WHERE teacher_id = ?"
        self.cursor.execute(query, (teacher_id,))
        if self.cursor.rowcount == 0:
            raise TeacherNotFoundException(f"Teacher with ID {teacher_id} not found.")
        self.conn.commit()
