import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher
from entity.enrollment import Enrollment
from entity.payment import Payment
from exception.custom_exeption import (
    StudentNotFoundException,
    CourseNotFoundException,
    DuplicateEnrollmentException,
    TeacherNotFoundException,
    PaymentValidationException
)

class SIS:
    def __init__(self):
        self.students = []
        self.courses = []
        self.teachers = []

    def enroll_student_in_course(self, student, course):
        if student not in self.students:
            raise StudentNotFoundException(f"Student with ID {student.student_id} not found.")

        if course not in self.courses:
            raise CourseNotFoundException(f"Course with ID {course.course_id} not found.")

        if student.student_id in course.enrollments:
            raise DuplicateEnrollmentException(f"Student {student.student_id} is already enrolled in course {course.course_id}.")

        student.enroll_in_course(course)
        course.enrollments.append(student.student_id)

    def assign_teacher_to_course(self, teacher, course):
        if teacher not in self.teachers:
            raise TeacherNotFoundException(f"Teacher with ID {teacher.teacher_id} not found.")

        if course not in self.courses:
            raise CourseNotFoundException(f"Course with ID {course.course_id} not found.")

        course.assign_teacher(teacher)
        if not hasattr(teacher, 'assigned_courses'):
            teacher.assigned_courses = []
        teacher.assigned_courses.append(course.course_id)

    def record_payment(self, student, amount, date):
        if student not in self.students:
            raise StudentNotFoundException(f"Student with ID {student.student_id} not found.")

        if amount <= 0:
            raise PaymentValidationException("Payment amount must be greater than zero.")

        student.make_payment(amount, date)

    def generate_enrollment_report(self, course):
        if course not in self.courses:
            raise CourseNotFoundException(f"Course with ID {course.course_id} not found.")
        return course.get_enrollments()

    def generate_payment_report(self, student):
        if student not in self.students:
            raise StudentNotFoundException(f"Student with ID {student.student_id} not found.")
        return student.get_payment_history()

    def calculate_course_statistics(self, course):
        if course not in self.courses:
            raise CourseNotFoundException(f"Course with ID {course.course_id} not found.")

        total_enrollments = len(course.enrollments)
        return {
            "course_id": course.course_id,
            "enrollments": total_enrollments
        }
