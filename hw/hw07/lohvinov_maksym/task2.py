import math
shape_choice = input("Choose a shape (1-Rectangle, 2-Triangle, 3-Circle):")

if shape_choice == "1":
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    area = width * height
    print(f"The area is: {area}")
elif shape_choice == "2":
    height = float(input("Enter height: "))
    base = float(input("Enter base: "))
    area = 0.5 * height * base
    print(f"The area is: {area}")
elif shape_choice == "3":
    radius = float(input("Enter radius: "))
    area = math.pi * (radius**2)
    print(f"The area is: {area}")
else:
    print("Invalid choice! Please enter 1, 2, or 3.")