import re

def check_password(user_password):
        if len(user_password) < 8:
                print("- Password does not contain more than 8 characters")

        if not re.search(r'[A-Z]', user_password):
                print("- Password does not contain at least one upper case letter.")

        if not re.search(r'[a-z]', user_password):
                print("- Password does not contain at least one lower case letter.")

        if not re.search(r'[0-9]', user_password):
                print("- Password does not contain at least one number.")

        if not re.search(r'[!@#$%^&*()_+,.?":{}|><]', user_password):
                print("- Password does not contain at least one special character.")
                
        if re.search(r'[!@#$%^&*()_+,.?":{}|><]', user_password) and re.search(r'[0-9]', user_password) and re.search(r'[a-z]', user_password) and re.search(r'[A-Z]', user_password) and len(user_password) > 8:
                return True        
        
while True:
        user_password = input("Enter a password to check its strength: ")
        is_valid = check_password(user_password)

        if is_valid:
                print("Your password strength is good.")
        else:
                print("Your password does not meet the requirements.")
