from file_handler import load_students, load_teachers

def generate_full_report():
    print("\n--- Full Analysis & Summary Report ---")
    students = load_students()
    teachers = load_teachers()

    if not students or not teachers:
        print("Could not generate report. Student or teacher data is missing.")
        return

    print("\nStudent-Teacher Report (based on student's best subject):")
    teacher_subject_map = {t.subject.lower(): t.name for t in teachers}
    for student in students:
        if student.marks:
            best_subject = max(student.marks, key=student.marks.get)
            teacher_name = teacher_subject_map.get(best_subject.lower(), "N/A")
            print(f"  Student: {student.name}, Best Subject: {best_subject}, Teacher: {teacher_name}")

    print("\n--- Summary Statistics ---")
    
    grade_counts = {}
    for student in students:
        grade_counts[student.grade] = grade_counts.get(student.grade, 0) + 1
    print("\nStudents per Grade:")
    for grade, count in sorted(grade_counts.items()):
        print(f"  Grade {grade}: {count} student(s)")

    subject_marks = {}
    subject_counts = {}
    for student in students:
        for subject, mark in student.marks.items():
            subject_marks[subject] = subject_marks.get(subject, 0) + mark
            subject_counts[subject] = subject_counts.get(subject, 0) + 1
    print("\nAverage Marks per Subject:")
    for subject, total in sorted(subject_marks.items()):
        avg = total / subject_counts[subject]
        print(f"  {subject}: {avg:.2f}")

    total_salary_spent = sum(t.salary for t in teachers)
    print(f"\nTotal Salary Expenditure on Teachers: ${total_salary_spent:,.2f}")
    print("-" * 35)