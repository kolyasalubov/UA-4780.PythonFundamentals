import re

if __name__ == '__main__':
    password_rules = (
        'At least 1 letter between [a-z] and 1 letter between [A-Z]\n'
        'At least 1 number between [0-9]\n'
        'At least 1 character between [$#@]\n'
        'Length between 6 and 16'
    )
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\$#@]).{6,16}$'
    password = input("Enter password to check: ").strip()

    if re.match(pattern, password):
        print('\nPassword is valid')
    else:
        print('\nPassword is invalid. It should match the following rules:\n', password_rules)
