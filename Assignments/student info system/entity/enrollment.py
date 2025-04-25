class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id, enrollment_date=None):
        from datetime import datetime
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date or datetime.now().date()
    def __str__(self):
        return f"Enrollment ID: {self.enrollment_id}, Student ID: {self.student_id}, Course ID: {self.course_id}, Date: {self.enrollment_date}"


    def get_student(self):
        return self.student_id

    def get_course(self):
        return self.course_id
