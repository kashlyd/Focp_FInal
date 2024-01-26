# login.py
from password_utilitys import read_password_file, find_user, decrypt_password
import getpass

def login():
    users = read_password_file()

    username = input("User: ")
    password = getpass.getpass("Password: ")  # Password input is now hidden

    user = find_user(username, users)
    # Check if the user exists and the password matches
    if user and decrypt_password(user[2]) == password:
        print("Access granted.")
    else:
        print("Access denied.")

if __name__ == "__main__":
    login()
