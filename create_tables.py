from db_connection import get_db_connection
import mysql.connector
def create_tables():
    connection= get_db_connection()
    if connection is None:
        return
    try:
        cursor= connection.cursor()
        create_a_student_table= """
                        CREATE TABLE IF NOT EXISTS students(
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        age INT NOT NULL,
                        course VARCHAR(50) NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );"""
        cursor.execute(create_a_student_table)
        connection.commit()
        print("'students' TABLE IS CREATED SUCCESSFULLY.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unknown Error: {e}")
    finally:
        cursor.close()
        connection.close()
        
if __name__== "__main__":
    create_tables()