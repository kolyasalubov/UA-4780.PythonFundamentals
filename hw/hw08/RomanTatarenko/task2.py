"""
Write a Python program to check the validity of a password
(input from users)
Validation:
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""
import re


def is_password_valid(password: str) -> bool:
    """
    Check if a password is valid.

    A valid password must have:
    - At least one lowercase letter [a-z]
    - At least one uppercase letter [A-Z]
    - At least one digit [0-9]
    - At least one special character [$#@]
    - Length between 6 and 16 characters
    """
    result = re.findall(f'[a-z]', password)
    if len(result) < 1:
        return False

    result = re.findall(r'[A-Z]', password)
    if len(result) < 1:
        return False

    result = re.findall(r'[0-9]', password)
    if len(result) < 1:
        return False

    result = re.findall(r'[$#@]', password)
    if len(result) < 1:
        return False

    password_length = len(password)
    if password_length < 6:
        return False

    if password_length > 16:
        return False

    return True


if __name__ == '__main__':
    user_password = input("Enter your password: ")
    is_valid = is_password_valid(user_password)
    print(
        "Your password is valid." if is_valid
        else "Your password is invalid."
    )
