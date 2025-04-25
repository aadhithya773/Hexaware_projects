class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}"
    

    def update_teacher_info(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def display_teacher_info(self):
        print(f"Teacher ID: {self.teacher_id}\nName: {self.first_name} {self.last_name}\nEmail: {self.email}")

    def get_assigned_courses(self):
        return self.assigned_courses
