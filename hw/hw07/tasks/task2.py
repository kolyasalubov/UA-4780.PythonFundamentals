import math

def rectangle_area(a, b):
    return a * b

def triangle_area(b, h):
    return 0.5 * b * h

def circle_area(r):
    return math.pi * r**2

print("Choose a shape:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")
choice = input("Your choice: ")

if choice == '1':
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    print(f"Area: {rectangle_area(a, b)}")
elif choice == '2':
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print(f"Area: {triangle_area(b, h)}")
elif choice == '3':
    r = float(input("Enter radius: "))
    print(f"Area: {circle_area(r)}")
else:
    print("Invalid choice.")