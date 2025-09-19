class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, id, name, age, grade, marks):
        super().__init__(name, age)
        self.id = id
        self.grade = grade
        self.marks = marks

    def get_average(self):
        return sum(self.marks.values()) / len(self.marks) if self.marks else 0

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Grade: {self.grade}"


class Teacher(Person):
    def __init__(self, id, name, subject, salary):
        super().__init__(name, age=None)
        self.id = id
        self.subject = subject
        self.salary = float(salary)

    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}, Subject: {self.subject}, Salary: ${self.salary:,.2f}"