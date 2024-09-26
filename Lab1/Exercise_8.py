import re
def is_valid_password(password):
    if len(password) < 8:
        print ("less 8 character")
        return 
    if not re.search(r'[A-Z]', password):
        print ("No character uppercase")
        return 
    if not re.search(r'[a-z]', password):
        print ("No character lowercase")
        return 
    if not re.search(r'[0-9]', password):
        print ("No number")
        return 
    if not re.search(r'[@&!#$%^&*(),.?":{}|<>]', password):
        print ("No special character")
        return 

    print ("Valid password")

    password = input("Enter a password to check: ")
    is_valid_password(password)