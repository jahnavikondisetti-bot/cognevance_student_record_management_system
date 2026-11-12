
from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

from reports import (
    performance_summary,
    class_statistics,
    individual_student_report
)


# =====================================
# MAIN APPLICATION
# =====================================

def main():

    while True:

        print("\n")
        print("=" * 45)
        print("       STUDENT RECORD MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Student Performance Report")
        print("7. Class Statistics")
        print("8. Individual Student Report")
        print("9. Exit")

        print("=" * 45)

        choice = input("\nEnter your choice (1-9): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            performance_summary()

        elif choice == "7":
            class_statistics()

        elif choice == "8":
            individual_student_report()

        elif choice == "9":
            print("\nThank you for using Student Record Management System!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please select between 1 and 9.")


# =====================================
# PROGRAM EXECUTION
# =====================================

if __name__ == "__main__":
    main()
