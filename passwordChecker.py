"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 10
SPECIAL_CHARS_REQUIRED = False
SPECIALS = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIALS)
    password = input(">>> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input(">>> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    passwordLength = len(password)
    if passwordLength < MIN_LENGTH:
        print("\tYour password must be more than {} characters" .format(MIN_LENGTH))
        return False
    elif passwordLength > MAX_LENGTH:
        print("\tYour password must be less than {} characters" .format(MAX_LENGTH))
        return False


    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    import string
    for char in password:
        if char.lower in string.ascii_lowercase:
            count_lower += 1
        if char.upper in string.ascii_uppercase:
            count_upper += 1
        if char.digit in string.ascii_number:
            count_digit += 1

       #count_lower = sum(1 for character in password if char.lower())
        #count_upper = sum(1 for character in password if char.upper())
        #count_digit = sum(1 for character in password if char.isnumeric())


    if count_lower >=1:
        if count_upper >=1:
            if count_digit >=1:
                passwordValid = True
                return True
            else:
                return False
        else:
            return False

    else:
        passwordValid = False
        return False

"""
        while not passwordValid:
            if password.lower() == password or password.upper() == password or password.isalnum() == password:
                count_lower = count_lower + 1
                count_upper = count_upper + 1
                count_digit = count_digit + 1
                passwordValid = True """


    # TODO: if any of the 'normal' counts are zero, return False

    # TODO: if special characters are required, then check the count of those and return False if it's zero



main()