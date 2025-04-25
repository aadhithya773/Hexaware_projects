import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.student_dao import StudentDAO
from dao.course_dao import CourseDAO
from dao.teacher_dao import TeacherDAO
from dao.enrollment_dao import EnrollmentDAO
from dao.payment_dao import PaymentDAO
from datetime import datetime

def print_menu():
    print("\n--- Student Information System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Add Course")
    print("4. View All Courses")
    print("5. Add Teacher")
    print("6. View All Teachers")
    print("7. Enroll Student in Course")
    print("8. View All Enrollments")
    print("9. Record Payment")
    print("10. View All Payments")
    print("0. Exit")

def main():
    student_dao = StudentDAO()
    course_dao = CourseDAO()
    teacher_dao = TeacherDAO()
    enrollment_dao = EnrollmentDAO()
    payment_dao = PaymentDAO()

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            first = input("First Name: ")
            last = input("Last Name: ")
            dob = input("DOB (YYYY-MM-DD): ")
            email = input("Email: ")
            phone = input("Phone: ")
            student_dao.add_student(first, last, dob, email, phone)
        
        elif choice == '2':
            students = student_dao.get_all_students()
            for student in students:
                print(student)
        
        elif choice == '3':
            name = input("Course Name: ")
            code = input("Course Code: ")
            teacher_id = int(input("Teacher ID: "))
            course_dao.add_course(name, code, teacher_id)

        elif choice == '4':
            courses = course_dao.get_all_courses()
            for course in courses:
                print(course)
        
        elif choice == '5':
            first = input("First Name: ")
            last = input("Last Name: ")
            email = input("Email: ")
            teacher_dao.add_teacher(first, last, email)
        
        elif choice == '6':
            teachers = teacher_dao.get_all_teachers()
            for teacher in teachers:
                print(teacher)

        elif choice == '7':
            student_id = int(input("Student ID: "))
            course_id = int(input("Course ID: "))
            date = input("Enrollment Date (YYYY-MM-DD): ")
            enrollment_dao.add_enrollment(student_id, course_id, date)

        elif choice == '8':
            enrollments = enrollment_dao.get_all_enrollments()
            for enrollment in enrollments:
                print(enrollment)

        elif choice == '9':
            student_id = int(input("Student ID: "))
            amount = float(input("Amount: "))
            date = input("Payment Date (YYYY-MM-DD): ")
            payment_dao.add_payment(student_id, amount, date)

        elif choice == '10':
            payments = payment_dao.get_all_payments()
            for payment in payments:
                print(payment)

        elif choice == '0':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
