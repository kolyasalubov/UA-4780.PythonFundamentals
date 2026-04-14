

"""
EX_2
Write a Python program to check the validity of a password (input from users).
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimumlength 6 characters.
Maximumlength 16 characters.
"""

import re

def password_check(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$"
    result = re.fullmatch(pattern, password)
    return result
    

password = input("Enter your password: ")

print("Successful login" if password_check(password) else "Incorrect password")



