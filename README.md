# 🎓 Student Management API

A **role-based backend Student Management application** developed using **Python** and **MySQL**.
This project is designed to manage student records securely with proper access control and analytics.

---

## 📌 Project Overview

The system supports **two user roles**:

### 👤 Admin
- Manages student records
- Performs CRUD operations
- Searches and filters students
- Views analytical insights

### 👨‍🎓 Student
- Logs in using Student ID
- Can view only personal details (read-only access)

---

## 🚀 Key Features

### Admin Features
- Admin authentication
- Add new students
- Update student information
- Search students by name
- Search students by course
- Filter students by age range
- Analytics:
  - Total number of students
  - Students per course
  - Average age
  - Most popular course

### Student Features
- Secure login using student ID
- View own profile details
- Restricted from modifying data

---

## 🛠️ Tech Stack

- Python
- MySQL
- mysql-connector-python
- python-dotenv
- Git & GitHub

---

## 🗂️ Project Structure

student-management-api/
│
├── main.py
├── db_connection.py
├── student_crud.py
├── create_db.py
├── create_tables.py
├── requirements.txt
│
├── auth/
│ ├── admin_auth.py
│ └── student_auth.py
│
├── utils/
│ ├── input_helpers.py
│ └── validators.py
│
└── .env (ignored using .gitignore)



---

## 🔐 Security Practices

- Database credentials stored in `.env`
- `.env` excluded using `.gitignore`
- Role-based access control (Admin & Student)
- Input validation for stability and safety

---

## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Create database and tables:
python create_db.py
python create_tables.py

3. Run the application:
python main.py

📊 Analytics & Insights
The application uses SQL aggregation queries to provide:
Total student count
Course-wise distribution
Age statistics
Popular course analysis

🔮 Future Enhancements
Password hashing

Database-based authentication

Logging and audit tracking

REST API using Flask or FastAPI

Web-based frontend integration

✅ Conclusion
This project demonstrates:

Backend application design

Role-based authentication

Database integration

Analytical queries

Clean modular coding practices
