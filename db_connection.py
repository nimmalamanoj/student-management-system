from dotenv import load_dotenv
import os
import mysql.connector

# Load variables from .env file
load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("STUDENT_DB_HOST"),
            user=os.getenv("STUDENT_DB_USER"),
            password=os.getenv("STUDENT_DB_PASSWORD"),
            database=os.getenv("STUDENT_DB_NAME")
        )
        return connection
    except mysql.connector.Error as err:
        print("Database connection error:", err)
        return None
