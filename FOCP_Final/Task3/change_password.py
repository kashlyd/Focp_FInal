# passwd.py
from password_utilitys import read_password_file, write_password_file, find_user, encrypt_password, decrypt_password
import getpass
def change_password():
    # Load the user data from the password file
    users = read_password_file()
    # Prompt the user to enter their username
    username = input("Enter Username: ")
    # Find the user in the list
    user = find_user(username, users)

     # Check if the user exists
    if not user:
        print("User not found.")
        return

    # Securely ask for the current password then Valides the current password
    current_password = getpass.getpass("Current Password: ")
    if decrypt_password(user[2]) != current_password:
        print("Invalid current password.")
        return

    # Securely ask for a new password and asks to confirm it, then confirms it
    new_password = getpass.getpass("New Password: ")
    confirm_password = getpass.getpass("Confirm Password: ")

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

     # Encrypt and update the user's password then write the updated user data back to the file
    user[2] = encrypt_password(new_password)
    write_password_file(users)
    print("Password changed.")

if __name__ == "__main__":
    change_password()
