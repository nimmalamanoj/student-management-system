ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


def admin_login():
    print("\n--- Admin Login ---")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Admin login successful")
        return True
    else:
        print("Invalid admin credentials")
        return False
