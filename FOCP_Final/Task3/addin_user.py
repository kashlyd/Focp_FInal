# adduser.py
from password_utilitys import read_password_file, write_password_file, find_user, encrypt_password
import getpass

def add_user():
     # Read existing users from the password file
    users = read_password_file()

    # Prompt for the new username
    username = input("Enter new username: ")
    
    # Check if the username already exists
    if find_user(username, users):
        print("Cannot add. Username already exists.")
        return

    # Prompt for the user's real name
    real_name = input("Enter real name: ")
    # Secure the password by not displaying whats typed then ncrypt the password for security
    password = getpass.getpass("Enter a password: ")
    encrypted_password = encrypt_password(password)

    # Add the new user to the list then write the updated list back to the file
    users.append([username, real_name, encrypted_password])
    write_password_file(users)
    print("User Created.")

if __name__ == "__main__":
    add_user()
