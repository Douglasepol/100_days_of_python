'''
Problem: Password Validation

Write a Python program to check the validity of a password based on certain criteria:
- At least 1 letter between [a-z] and 1 letter between [A-Z].
- At least 1 number between [0-9].
- At least 1 character from [$#@].
- Minimum length of 6 characters.
- Maximum length of 16 characters.

Parameters:
password (str): The password to be validated.

Returns:
str: A message indicating whether the password is valid or not.
'''

import re

def validate_password(password):
    if (6 <= len(password) <= 16 and 
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[$#@]", password) and
        not re.search("\s", password)):
        return "Valid Password"
    else:
        return "Not a Valid Password"

# Test examples
test_passwords = ["W3r@100a", "abc", "12345", "Abc@1", "VeryLongInvalidPasswordOver16Chars"]

# Iterate through each password and validate it
for pwd in test_passwords:
    result = validate_password(pwd)
    print(f"Password '{pwd}': {result}")
