from db_connection import get_db_connection
from utils.input_helpers import get_int_input


def student_login():
    print("\n--- Student Login ---")

    # Student enters ID safely
    student_id = get_int_input("Enter your student ID: ")

    connection = get_db_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, name, age, course FROM students WHERE id = %s",
            (student_id,)
        )
        student = cursor.fetchone()

        if student:
            print(f"\n Welcome {student[1]}")
            return student
        else:
            print("Student not found.")
            return None

    except Exception as e:
        print("Error during student login:", e)
        return None

    finally:
        cursor.close()
        connection.close()
