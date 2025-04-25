class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.enrollments = []
        self.payments = []
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.first_name} {self.last_name}, DOB: {self.date_of_birth}, Email: {self.email}, Phone: {self.phone_number}"


    def enroll_in_course(self, course):
        from entity.enrollment import Enrollment
        enrollment = Enrollment(len(self.enrollments) + 1, self.student_id, course.course_id)
        self.enrollments.append(enrollment)

    def update_student_info(self, first_name, last_name, dob, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = dob
        self.email = email
        self.phone_number = phone_number

    def make_payment(self, amount, payment_date):
        from entity.payment import Payment
        payment = Payment(len(self.payments) + 1, self.student_id, amount, payment_date)
        self.payments.append(payment)

    def display_student_info(self):
        print(f"Student ID: {self.student_id}\nName: {self.first_name} {self.last_name}\nDOB: {self.date_of_birth}\nEmail: {self.email}\nPhone: {self.phone_number}")

    def get_enrolled_courses(self):
        return [enr.course_id for enr in self.enrollments]

    def get_payment_history(self):
        return self.payments
