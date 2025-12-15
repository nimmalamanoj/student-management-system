from auth.admin_auth import admin_login
from auth.student_auth import student_login

from student_crud import (
    add_student,
    update_student,
    search_student_by_name,
    search_students_by_course,
    filter_students_by_age,
    get_total_students,
    get_students_per_course,
    get_average_age,
    get_most_popular_course
)

from utils.input_helpers import get_int_input, get_optional_int_input


# ---------- MENUS ----------

def start_app():
    print("\n===== Student Management System =====")
    print("1. Admin Login")
    print("2. Student Login")
    print("3. Exit")

    choice = input("Select role: ")

    if choice == "1":
        admin_main()
    elif choice == "2":
        student_view()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice")


def show_menu():
    print("\n===== Admin Menu =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Search Student by Name")
    print("4. Search Students by Course")
    print("5. Filter Students by Age")
    print("6. Analytics & Insights")
    print("7. Exit")


def analytics_menu():
    print("\n--- Analytics & Insights ---")
    print("1. Total Students")
    print("2. Students per Course")
    print("3. Average Age")
    print("4. Most Popular Course")
    print("5. Back")


# ---------- STUDENT VIEW ----------

def student_view():
    student = student_login()
    if not student:
        return

    print("\n--- Student Details ---")
    print(f"ID     : {student[0]}")
    print(f"Name   : {student[1]}")
    print(f"Age    : {student[2]}")
    print(f"Course : {student[3]}")


# ---------- ADMIN FLOW ----------

def admin_main():
    if not admin_login():
        return

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = get_int_input("Enter age: ")
            course = input("Enter course: ")
            add_student(name, age, course)

        elif choice == "2":
            student_id = get_int_input("Enter student ID: ")
            name = input("Enter new name (press Enter to skip): ") or None
            age = get_optional_int_input("Enter new age (press Enter to skip): ")
            course = input("Enter new course (press Enter to skip): ") or None
            update_student(student_id, name, age, course)

        elif choice == "3":
            name = input("Enter name to search: ")
            search_student_by_name(name)

        elif choice == "4":
            course = input("Enter course name: ")
            search_students_by_course(course)

        elif choice == "5":
            min_age = get_int_input("Enter minimum age: ")
            max_age = get_int_input("Enter maximum age: ")
            filter_students_by_age(min_age, max_age)

        elif choice == "6":
            while True:
                analytics_menu()
                a_choice = input("Enter analytics choice: ")

                if a_choice == "1":
                    get_total_students()
                elif a_choice == "2":
                    get_students_per_course()
                elif a_choice == "3":
                    get_average_age()
                elif a_choice == "4":
                    get_most_popular_course()
                elif a_choice == "5":
                    break
                else:
                    print("Invalid analytics choice")

        elif choice == "7":
            print("Exiting admin panel.")
            break

        else:
            print("Invalid choice. Try again.")


# ---------- ENTRY POINT ----------

if __name__ == "__main__":
    start_app()
