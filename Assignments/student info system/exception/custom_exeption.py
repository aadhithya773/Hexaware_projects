# exception/custom_exceptions.py

class DuplicateEnrollmentException(Exception):
    def __init__(self, message="Student is already enrolled in this course."):
        super().__init__(message)

class CourseNotFoundException(Exception):
    def __init__(self, message="The specified course was not found."):
        super().__init__(message)

class StudentNotFoundException(Exception):
    def __init__(self, message="The specified student was not found."):
        super().__init__(message)

class TeacherNotFoundException(Exception):
    def __init__(self, message="The specified teacher was not found."):
        super().__init__(message)

class PaymentValidationException(Exception):
    def __init__(self, message="Invalid payment details."):
        super().__init__(message)

class InvalidStudentDataException(Exception):
    def __init__(self, message="Invalid student data provided."):
        super().__init__(message)

class InvalidCourseDataException(Exception):
    def __init__(self, message="Invalid course data provided."):
        super().__init__(message)

class InvalidEnrollmentDataException(Exception):
    def __init__(self, message="Invalid enrollment data provided."):
        super().__init__(message)

class InvalidTeacherDataException(Exception):
    def __init__(self, message="Invalid teacher data provided."):
        super().__init__(message)

class InsufficientFundsException(Exception):
    def __init__(self, message="Student has insufficient funds for enrollment."):
        super().__init__(message)
