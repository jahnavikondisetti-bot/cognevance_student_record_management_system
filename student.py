
from file_handler import load_students, save_students


# =====================================
# 1. ADD STUDENT
# =====================================

def add_student():

    students = load_students()

    print("\n========== ADD NEW STUDENT ==========")

    student_id = input("Enter Student ID: ").strip().upper()

    if not student_id:
        print("Student ID cannot be empty!")
        return

    # Check duplicate ID
    for student in students:
        if student["student_id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty!")
        return

    try:
        age = int(input("Enter Student Age: "))

        if age <= 0:
            print("Age must be positive!")
            return

        course = input("Enter Course: ").strip()

        if not course:
            print("Course cannot be empty!")
            return

        marks = float(input("Enter Marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100!")
            return

    except ValueError:
        print("Please enter valid numeric values!")
        return

    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    if save_students(students):
        print("\nStudent added successfully!")


# =====================================
# 2. VIEW ALL STUDENTS
# =====================================

def view_students():

    students = load_students()

    print("\n========== ALL STUDENT RECORDS ==========")

    if not students:
        print("No student records found!")
        return

    print("-" * 75)

    print(
        f"{'ID':<12}"
        f"{'NAME':<22}"
        f"{'AGE':<8}"
        f"{'COURSE':<15}"
        f"{'MARKS':<10}"
    )

    print("-" * 75)

    for student in students:

        print(
            f"{student['student_id']:<12}"
            f"{student['name']:<22}"
            f"{student['age']:<8}"
            f"{student['course']:<15}"
            f"{student['marks']:<10}"
        )

    print("-" * 75)

    print("Total Students:", len(students))


# =====================================
# 3. SEARCH STUDENT
# =====================================

def search_student():

    students = load_students()

    print("\n========== SEARCH STUDENT ==========")

    student_id = input("Enter Student ID: ").strip().upper()

    for student in students:

        if student["student_id"] == student_id:

            print("\nStudent Found!")

            print("Student ID:", student["student_id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])

            return

    print("Student not found!")


# =====================================
# 4. UPDATE STUDENT
# =====================================

def update_student():

    students = load_students()

    print("\n========== UPDATE STUDENT ==========")

    student_id = input("Enter Student ID: ").strip().upper()

    for student in students:

        if student["student_id"] == student_id:

            print("\nStudent Found!")
            print("Press Enter to keep the existing value.")

            new_name = input(
                f"Enter Name [{student['name']}]: "
            ).strip()

            if new_name:
                student["name"] = new_name

            new_age = input(
                f"Enter Age [{student['age']}]: "
            ).strip()

            if new_age:
                try:
                    age = int(new_age)

                    if age <= 0:
                        print("Age must be positive!")
                        return

                    student["age"] = age

                except ValueError:
                    print("Invalid age!")
                    return

            new_course = input(
                f"Enter Course [{student['course']}]: "
            ).strip()

            if new_course:
                student["course"] = new_course

            new_marks = input(
                f"Enter Marks [{student['marks']}]: "
            ).strip()

            if new_marks:
                try:
                    marks = float(new_marks)

                    if not 0 <= marks <= 100:
                        print("Marks must be between 0 and 100!")
                        return

                    student["marks"] = marks

                except ValueError:
                    print("Invalid marks!")
                    return

            if save_students(students):
                print("\nStudent updated successfully!")

            return

    print("Student not found!")


# =====================================
# 5. DELETE STUDENT
# =====================================

def delete_student():

    students = load_students()

    print("\n========== DELETE STUDENT ==========")

    student_id = input("Enter Student ID: ").strip().upper()

    for student in students:

        if student["student_id"] == student_id:

            print("\nStudent Found!")
            print("Name:", student["name"])

            confirm = input(
                "Are you sure you want to delete? (yes/no): "
            ).strip().lower()

            if confirm == "yes":

                students.remove(student)

                if save_students(students):
                    print("\nStudent deleted successfully!")

            else:
                print("Deletion cancelled!")

            return

    print("Student not found!")

