import random
import string

def genPassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

passwordLength = int(input("How many characters do you want your password to be?"))
password = genPassword(passwordLength)
print(f"Your new generated password is: {password}")
