import random
import string

def password_generator(length,uppercase,lowercase,numbers,special):
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
    try:
        choix = input("Do you want to generate a password? (y/n): ")
        assert choix == "y" or choix == "n"
    except AssertionError:
        print("Please enter 'y' or 'n'.")
        continue
    print("--------------------------------------------------")

    if choix == "n":
        break

    while True:
        try:
            length = int(input("Enter the length of the password: "))
        except ValueError:
            print("Please enter a number.")
        else:
            break

    while True:
        uppercase = input("Do you want uppercase letters in the password? (y/n): ")
        if uppercase == "y" or uppercase == "n":
            break
        else:
            print("Please enter 'y' or 'n'.")

    while True:
        lowercase = input("Do you want lowercase letters in the password? (y/n): ")
        if lowercase == "y" or lowercase == "n":
            break
        else:
            print("Please enter 'y' or 'n'.")

    while True:
        numbers = input("Do you want numbers in the password? (y/n): ")
        if numbers == "y" or numbers == "n":
            break
        else:
            print("Please enter 'y' or 'n'.")

    while True:
        special = input("Do you want special characters in the password? (y/n): ")
        if special == "y" or special == "n":
            break
        else:
            print("Please enter 'y' or 'n'.")

    uppercase = True if uppercase == "y" else False
    lowercase = True if lowercase == "y" else False
    numbers = True if numbers == "y" else False
    special = True if special == "y" else False

    password = password_generator(length,uppercase,lowercase,numbers,special)

    print("Your password is: {}".format(password))

print("Goodbye!")