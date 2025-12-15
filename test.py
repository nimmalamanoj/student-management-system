# from db_connection import get_db_connection

# conn= get_db_connection()

# if conn:
#     print("database connection succesful")
#     conn.close()
# else:
#     print("Database connection failed")

# from student_crud import add_student, view_all_students

# add_student("Sriramula Sahith", 24, "Data Analyst")
# add_student("Chiluveri Jaish", 22, "Full Stack Python")

# view_all_students()

from student_crud import (
    get_total_students,
    get_students_per_course,
    get_average_age,
    get_most_popular_course
)

get_total_students()
get_students_per_course()
get_average_age()
get_most_popular_course()
