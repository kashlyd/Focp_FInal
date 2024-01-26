# password_utils.py
import codecs

PASSWORD_FILE = 'passwd.txt'

def read_password_file():
    """
    This funciton opens and reads the password file and returns a list where each item is a user's details.
    Each record is a list containing the username, real name, and encrypted password, split by ':'.
    """
    with open(PASSWORD_FILE, 'r') as file:
        return [line.strip().split(':') for line in file]

def write_password_file(users):
    """
    This funciton writes the user records to the main password file.
    Each user's information is joined by ':' and written on separate lines.
    """
    with open(PASSWORD_FILE, 'w') as file:
        for user in users:
            file.write(':'.join(user) + '\n')

def find_user(username, users):
    """
    This funciton searches for a user by username in the list of users.
    Returns the user's record if found, None otherwise.
    """
    return next((user for user in users if user[0] == username), None)

def encrypt_password(password):
    #Encrypts a password using ROT13 cipher
    return codecs.encode(password, 'rot_13')

def decrypt_password(encrypted_password):
    #Decrypts a password encrypted with ROT13 cipher.
    return codecs.encode(encrypted_password, 'rot_13')

def check_password(stored_user, input_password):
    # This checks if the provided input_password matches the stored user's encrypted password
    encrypted_input_password = encrypt_password(input_password)
    return encrypted_input_password == stored_user[2]