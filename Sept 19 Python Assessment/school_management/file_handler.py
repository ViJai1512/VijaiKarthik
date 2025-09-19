import json
import csv
from models import Student, Teacher

def load_students(filename="students.json"):
    try:
        with open(filename, 'r') as f:
            students_data = json.load(f)
        return [Student(**data) for data in students_data]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def save_students(students, filename="students.json"):
    students_data = [
        {"id": s.id, "name": s.name, "age": s.age, "grade": s.grade, "marks": s.marks}
        for s in students
    ]
    with open(filename, 'w') as f:
        json.dump(students_data, f, indent=2)

def load_teachers(filename="teachers.csv"):
    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.DictReader(f)
            return [Teacher(**row) for row in reader]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def save_teachers(teachers, filename="teachers.csv"):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'subject', 'salary'])
        for t in teachers:
            writer.writerow([t.id, t.name, t.subject, t.salary])