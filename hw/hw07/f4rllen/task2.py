import math

def get_rectangle_area(a, b):
    return a * b

def get_triangle_area(base, height):
    return 0.5 * base * height

def get_circle_area(radius):
    return math.pi * (radius ** 2)

shape = input("Choose shape (1-rectangle, 2-triangle, 3-circle): ")

if shape == '1':
    print(get_rectangle_area(float(input()), float(input())))
elif shape == '2':
    print(get_triangle_area(float(input()), float(input())))
elif shape == '3':
    print(get_circle_area(float(input())))