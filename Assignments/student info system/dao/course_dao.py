# dao/course_dao.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from entity.course import Course
from util.db_conn_util import DBConnUtil
from exception.custom_exeption import CourseNotFoundException

class CourseDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()
    
    def get_all_courses(self):
        courses = []
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT course_id, course_name, credits, teacher_id FROM courses")
            rows = cursor.fetchall()
            for row in rows:
                courses.append(Course(*row))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
        return courses

    def add_course(self, course: Course):
        try:
            query = """
            INSERT INTO Courses (course_id, course_name, course_code, teacher_id)
            VALUES (?, ?, ?, ?)
            """
            self.cursor.execute(query, (
                course.course_id,
                course.course_name,
                course.course_code,
                course.teacher_id
            ))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def get_course_by_id(self, course_id):
        query = "SELECT * FROM Courses WHERE course_id = ?"
        self.cursor.execute(query, (course_id,))
        row = self.cursor.fetchone()
        if row:
            return Course(*row)
        else:
            raise CourseNotFoundException(f"Course with ID {course_id} not found.")

    def update_course(self, course: Course):
        query = """
        UPDATE Courses SET course_name = ?, course_code = ?, teacher_id = ?
        WHERE course_id = ?
        """
        self.cursor.execute(query, (
            course.course_name,
            course.course_code,
            course.teacher_id,
            course.course_id
        ))
        if self.cursor.rowcount == 0:
            raise CourseNotFoundException(f"Course with ID {course.course_id} not found.")
        self.conn.commit()

    def delete_course(self, course_id):
        query = "DELETE FROM Courses WHERE course_id = ?"
        self.cursor.execute(query, (course_id,))
        if self.cursor.rowcount == 0:
            raise CourseNotFoundException(f"Course with ID {course_id} not found.")
        self.conn.commit()
