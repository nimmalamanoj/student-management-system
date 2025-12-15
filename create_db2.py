import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("STUDENT_DB_HOST"),
    user=os.getenv("STUDENT_DB_USER"),
    password=os.getenv("STUDENT_DB_PASSWORD")
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS students_db")
print("Database created / already exists")

cursor.close()
conn.close()
