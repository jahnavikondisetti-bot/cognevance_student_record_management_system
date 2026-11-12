
from file_handler import load_students


# =====================================
# 1. CALCULATE STUDENT GRADE
# =====================================

def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 50:
        return "D"

    else:
        return "F"


# =====================================
# 2. STUDENT PERFORMANCE SUMMARY
# =====================================

def performance_summary():

    students = load_students()

    print("\n========== STUDENT PERFORMANCE REPORT ==========")

    if not students:
        print("No student records available!")
        return

    print(
        f"{'ID':<12}"
        f"{'NAME':<22}"
        f"{'MARKS':<12}"
        f"{'GRADE':<10}"
        f"{'RESULT':<10}"
    )

    print("-" * 66)

    for student in students:

        marks = float(student["marks"])

        grade = calculate_grade(marks)

        result = "Pass" if marks >= 50 else "Fail"

        print(
            f"{student['student_id']:<12}"
            f"{student['name']:<22}"
            f"{marks:<12.2f}"
            f"{grade:<10}"
            f"{result:<10}"
        )

    print("-" * 66)

    print("Total Students:", len(students))


# =====================================
# 3. CLASS STATISTICS
# =====================================

def class_statistics():

    students = load_students()

    print("\n========== CLASS STATISTICS ==========")

    if not students:
        print("No student records available!")
        return

    marks_list = [
        float(student["marks"])
        for student in students
    ]

    average = sum(marks_list) / len(marks_list)

    highest = max(
        students,
        key=lambda student: float(student["marks"])
    )

    lowest = min(
        students,
        key=lambda student: float(student["marks"])
    )

    print("\nTotal Students:", len(students))

    print(f"Average Marks: {average:.2f}")

    print(
        "Highest Marks:",
        highest["name"],
        "-",
        highest["marks"]
    )

    print(
        "Lowest Marks:",
        lowest["name"],
        "-",
        lowest["marks"]
    )

    print("\nClass statistics generated successfully!")


# =====================================
# 4. INDIVIDUAL STUDENT REPORT
# =====================================

def individual_student_report():

    students = load_students()

    print("\n========== INDIVIDUAL STUDENT REPORT ==========")

    if not students:
        print("No student records available!")
        return

    student_id = input("Enter Student ID: ").strip().upper()

    for student in students:

        if student["student_id"] == student_id:

            marks = float(student["marks"])

            grade = calculate_grade(marks)

            result = "Pass" if marks >= 50 else "Fail"

            print("\n------------- STUDENT REPORT -------------")

            print("Student ID :", student["student_id"])
            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Course     :", student["course"])
            print("Marks      :", marks)
            print("Grade      :", grade)
            print("Result     :", result)

            print("------------------------------------------")

            return

    print("Student not found!")
