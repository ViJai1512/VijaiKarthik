from models import Student, Teacher
from file_handler import load_students, save_students, load_teachers, save_teachers
from reports import generate_full_report

def view_all_students():
    students = load_students()
    print("\n--- All Students ---")
    if not students:
        print("No student data found.")
        return
    
    topper = max(students, key=lambda s: s.get_average())
    for student in students:
        is_topper = " (Class Topper)" if student.id == topper.id else ""
        print(f"{student}, Average: {student.get_average():.2f}{is_topper}")

def view_all_teachers():
    teachers = load_teachers()
    print("\n--- All Teachers ---")
    if not teachers:
        print("No teacher data found.")
        return
    
    highest_paid = max(teachers, key=lambda t: t.salary)
    for teacher in teachers:
        is_highest = " (Highest Paid)" if teacher.id == highest_paid.id else ""
        print(f"{teacher.get_details()}{is_highest}")

def add_new_student():
    students = load_students()
    try:
        id = max([s.id for s in students]) + 1 if students else 1
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        print("Enter marks for the following subjects:")
        math = int(input("  Math: "))
        science = int(input("  Science: "))
        english = int(input("  English: "))

        new_student = Student(id, name, age, grade, {"Math": math, "Science": science, "English": english})
        students.append(new_student)
        save_students(students)
        print(f"\nStudent '{name}' added successfully!")
    except ValueError:
        print("\nInvalid input. Please enter numbers for age and marks.")

def add_new_teacher():
    teachers = load_teachers()
    try:
        id = max([int(t.id) for t in teachers]) + 1 if teachers else 1
        name = input("Enter teacher name: ")
        subject = input("Enter teacher subject: ")
        salary = float(input("Enter teacher salary: "))

        new_teacher = Teacher(id, name, subject, salary)
        teachers.append(new_teacher)
        save_teachers(teachers)
        print(f"\nTeacher '{name}' added successfully!")
    except ValueError:
        print("\nInvalid input. Please enter a number for salary.")

def main():
    while True:
        print("\n===== 🏫 School Management System =====")
        print("1. View All Students")
        print("2. View All Teachers")
        print("3. Add New Student")
        print("4. Add New Teacher")
        print("5. Generate Full Analysis Report")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            view_all_students()
        elif choice == '2':
            view_all_teachers()
        elif choice == '3':
            add_new_student()
        elif choice == '4':
            add_new_teacher()
        elif choice == '5':
            generate_full_report()
        elif choice == '6':
            print("Exiting the application. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()