class Payment:
    def __init__(self, payment_id, student_id, amount, payment_date):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date
    
    def __str__(self):
        return f"Payment ID: {self.payment_id}, Student ID: {self.student_id}, Amount: {self.amount}, Date: {self.payment_date}"


    def get_student(self):
        return self.student_id

    def get_payment_amount(self):
        return self.amount

    def get_payment_date(self):
        return self.payment_date
