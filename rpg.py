import random
import string

def password_generator(length=8,uppercase=True,lowercase=True,numbers=False,special=False):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation

    password = "".join(random.choice(characters) for i in range(length))
    return password


while True:

    print("--------------------------------------------------")
    choix = input("Do you want to generate a password? (y/n): ")
    print("--------------------------------------------------")
    if choix == "n":
        break

    length = int(input("Enter the length of the password: "))
    uppercase = input("Do you want uppercase letters in the password? (y/n): ")
    lowercase = input("Do you want lowercase letters in the password? (y/n): ")
    numbers = input("Do you want numbers in the password? (y/n): ")
    special = input("Do you want special characters in the password? (y/n): ")

    uppercase = True if uppercase == "y" else False
    lowercase = True if lowercase == "y" else False
    numbers = True if numbers == "y" else False
    special = True if special == "y" else False

    password = password_generator(length,uppercase,lowercase,numbers,special)

    print("Your password is: {}".format(password))

print("Goodbye!")