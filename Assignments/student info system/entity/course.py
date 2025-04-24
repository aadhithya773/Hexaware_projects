class Course:
    def __init__(self, course_id, course_name,credits,teacher_id=None):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.teacher_id = teacher_id
        self.enrollments = []

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.course_name}, Credits: {self.credits}, Teacher ID: {self.teacher_id}"



    def assign_teacher(self, teacher):
        self.instructor = teacher

    def update_course_info(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor

    def display_course_info(self):
        print(f"Course ID: {self.course_id}\nCode: {self.course_code}\nName: {self.course_name}\nInstructor: {self.instructor.first_name if self.instructor else 'Not Assigned'}")

    def get_enrollments(self):
        return self.enrollments

    def get_teacher(self):
        return self.instructor
