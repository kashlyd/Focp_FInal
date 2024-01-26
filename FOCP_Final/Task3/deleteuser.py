# delete_user.py
from password_utilitys import read_password_file, write_password_file, find_user, check_password
import getpass
def delete_user():
    # Load the user data from the password file
    users = read_password_file()

    # Ask the user to enter their username that needs to be deleted
    username = input("Enter username: ")
    # Find the user in the list    
    user = find_user(username, users)

    # Check if the user exists
    if user:
        # Securely ask for the user's password for verification
        password = getpass.getpass("Enter password for verification: ")
        # Verify the password
        if check_password(user, password):
            # Remove the user from the list only password is correct            
            users.remove(user)
            # Write the updated list back to the file
            write_password_file(users)
            print("User Deleted.")
        else:
            # Tell the user if the password is incorrect
            print("Password incorrect. User not deleted.")
    else:
        # Tell the user if the username is not found
        print("User not found.")

if __name__ == "__main__":
    delete_user()
