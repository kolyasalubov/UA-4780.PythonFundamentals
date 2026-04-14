import re

print("Create a password. Password must be at least 1 capital and lower letter and 1 number, 1 charachter. Min length 6 char, max - 16")
upass = input("Enter password:")

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>])[A-Za-z\d!@#$%^&*(),.?\":{}|<>]{6,16}$"

if re.match(pattern, upass):
    print("Password is valid!")
else:
    print("Password is too weak or invalid length. Try again.")