import re


def is_valid_password(password):
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check if the password contains at least one numeric digit
    if not re.search(r'[0-9]', password):
        return False

    # Check if the password contains at least one special symbol
    if not re.search(r'[@&!#$%^&*(),.?":{}|<>]', password):
        return False

    return True


# Example usage
password = input("Enter a password to check: ")
if is_valid_password(password):
    print("The password is valid.")
else:
    print("The password is invalid.")