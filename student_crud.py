from db_connection import get_db_connection
from utils.validators import normalize_name, is_valid_age
import mysql.connector

#Duplicate checking
def student_exists(name: str) -> bool:
    connection = get_db_connection()
    if connection is None:
        return False

    cursor = connection.cursor()
    try:
        query = "SELECT COUNT(*) FROM students WHERE name = %s"
        cursor.execute(query, (name,))

        count = cursor.fetchone()[0]
        return count > 0
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


#Adding students
def add_student(name: str, age: int, course: str):

    # Normalize name
    name = normalize_name(name)

    # Validate age
    if not is_valid_age(age):
        print("Invalid age. Age must be between 5 and 100.")
        return

    # Duplicate check (STEP 1.3)
    if student_exists(name):
        print(f"Student '{name}' already exists.")
        return

    # Insert into database
    connection = get_db_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO students (name, age, course)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (name, age, course))
        connection.commit()

        print(f"Student '{name}' added successfully.")

    except Exception as e:
        print("Error while adding student:", e)

    finally:
        cursor.close()
        connection.close()
        
        
#View all registered students 
def view_all_students():
    connection= get_db_connection()
    if connection is None:
        return
    cursor= connection.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM students")
        count= cursor.fetchone()[0]
        print("="*30)
        print(f"\nTotal Students: {count[0]}\n")
        print("="*30)
        cursor.execute("""
                    SELECT id, name, age, course FROM students
                    """)
        response= cursor.fetchall()
        
        if not response:
            print("No students found.")    
        else:
            for student in response:
                print(f"Student ID: {student[0]}")
                print(f"Name: {student[1]}")
                print(f"Age: {student[2]}")
                print(f"Course: {student[3]}")
                print("-"*30)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unknown Error: {e}")
    finally:
        cursor.close()
        connection.close()   
        
        
# Update Student Details
def update_student(student_id: int, name: str = None, age: int = None, course: str = None):
    connection = get_db_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        # Check if student exists
        cursor.execute("SELECT name, age, course FROM students WHERE id = %s",
            (student_id,)
        )
        response = cursor.fetchone()

        if not response:
            print("Student not found.")
            cursor.close()
            connection.close()
            return

        old_name, old_age, old_course = response 

        # checking the new values
        if name is not None:
            name = normalize_name(name)
        else:
            name = old_name

        if age is not None:
            if not is_valid_age(age):
                print("Invalid age.")
                cursor.close()
                connection.close()
                return
        else:
            age = old_age

        if course is None:
            course = old_course

        # Check if anything changed
        if name == old_name and age == old_age and course == old_course:
            print("No changes detected. Nothing was updated.")
            cursor.close()
            connection.close()
            return

        # Update only when needed
        cursor.execute(
            """
            UPDATE students
            SET name = %s, age = %s, course = %s
            WHERE id = %s
            """,
            (name, age, course, student_id)
        )
        connection.commit()

        print("Student updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Error while updating: {e}")
    finally:
        cursor.close()
        connection.close()
 
 
# Deleting safely 
def delete_student(student_id: int):
    connection = get_db_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # Check if student exists
        cursor.execute(
            "SELECT id, name, age, course FROM students WHERE id = %s",
            (student_id,)
        )
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            cursor.close()
            connection.close()
            return

        # Show student details
        print("="*30)
        print("Student found")
        print("="*30)
        for s in student:
                    print(f"Student ID: {s[0]}")
                    print(f"Name: {s[1]}")
                    print(f"Age: {s[2]}")
                    print(f"Course: {s[3]}")
                    print("-"*30)

        # Confirmation
        confirm = input("Are you sure you want to delete this student? (yes/no): ").lower()
        if confirm != "yes":
            print("Deletion cancelled.")
            cursor.close()
            connection.close()
            return

        # Delete student
        cursor.execute(
            "DELETE FROM students WHERE id = %s",
            (student_id,)
        )
        connection.commit()

        print("Student deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error while deleting: {err}")
    except Exception as e:
        print(f"Error whikle deleting: {e}")
    finally:
        cursor.close()
        connection.close()
    

# Search Student By Name
def search_student_by_name(name: str):
    connection = get_db_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # normalize name before search
        name = normalize_name(name)

        query = """
        SELECT id, name, age, course
        FROM students
        WHERE name = %s
        """
        cursor.execute(query, (name,))
        students = cursor.fetchall()

        if not students:
            print("No student found with this name.")
        else:
            print("Student(s) found:")
            for student in students:
                print(student)
    except mysql.connector.Error as e:
        print(f"Error while searching: {e}")
    except Exception as e:
        print(f"Error while searching: {e}")
    finally:
        cursor.close()
        connection.close()

# search all students by course
def search_students_by_course(course: str):
    connection = get_db_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        # Total students count
        cursor.execute("SELECT COUNT(*) FROM students")
        count = cursor.fetchone()[0]
        print("=" * 30)
        print(f"Total Students: {count}")
        print("=" * 30)

        # Search by course
        query = """
        SELECT id, name, age, course
        FROM students
        WHERE course = %s
        """
        cursor.execute(query, (course,))
        students = cursor.fetchall()

        if not students:
            print("No students found for this course.")
        else:
            print(f"\nStudents enrolled in {course}:\n")
            for s in students:
                print(f"Student ID : {s[0]}")
                print(f"Name       : {s[1]}")
                print(f"Age        : {s[2]}")
                print(f"Course     : {s[3]}")
                print("-" * 30)

    except Exception as e:
        print("Error while searching students by course:", e)

    finally:
        cursor.close()
        connection.close()


# filter students by age range
def filter_students_by_age(min_age: int, max_age: int):
    connection = get_db_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
        SELECT id, name, age, course
        FROM students
        WHERE age BETWEEN %s AND %s
        """
        cursor.execute(query, (min_age, max_age))
        students = cursor.fetchall()

        if not students:
            print("No students found in this age range.")
        else:
            print(f"\nStudents between age {min_age} and {max_age}:\n")
            for s in students:
                print(f"Student ID : {s[0]}")
                print(f"Name       : {s[1]}")
                print(f"Age        : {s[2]}")
                print(f"Course     : {s[3]}")
                print("-" * 30)

    except Exception as e:
        print("Error while filtering students by age:", e)

    finally:
        cursor.close()
        connection.close()


#Total number of students
def get_total_students():
    connection = get_db_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM students")
        total = cursor.fetchone()[0]
        print(f"Total number of students: {total}")

    except Exception as e:
        print("Error while fetching total students:", e)

    finally:
        cursor.close()
        connection.close()


# Course and count of students registered for it
def get_students_per_course():
    connection = get_db_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
        SELECT course, COUNT(*) 
        FROM students
        GROUP BY course
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("="*30)
        print("Students per Course")
        print("-"*30)
        for course, count in results:
            print(f"{course} : {count}")
        print("="*30)

    except Exception as e:
        print(" Error while fetching course analytics:", e)

    finally:
        cursor.close()
        connection.close()


#Average age of students
def get_average_age():
    connection = get_db_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT AVG(age) FROM students")
        avg_age = cursor.fetchone()[0]

        if avg_age:
            print(f"Average student age: {avg_age:.2f}")

    except Exception as e:
        print("Error while calculating average age:", e)

    finally:
        cursor.close()
        connection.close()


# Which is most popular course
def get_most_popular_course():
    connection = get_db_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
        SELECT course, COUNT(*) AS total
        FROM students
        GROUP BY course
        ORDER BY total DESC
        LIMIT 1
        """
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            course, total = result
            print(f"Most popular course: {course} ({total} students)")

    except Exception as e:
        print("Error while fetching popular course:", e)

    finally:
        cursor.close()
        connection.close()
