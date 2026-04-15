

###
print("\nEX_2")
###

"""
Task2. Write a program that calculates the area of ​​a rectangle, 
triangle and circle 
(write three functions to calculate the area, and call them in the 
main program depending on the user's choice).

"""

def area_rectangle(a, b):
    return a * b

def area_triangle(a, h):
    return 0.5 * a * h

def area_circle(r):
    P = 3.14
    return P * r ** 2

var_of_fig = input("Choose your figure (1 - rectangle, 2 - triangle, 3 - circle): ")

match var_of_fig:
    case "1":
        a, b = list(map(int, input("Enter the values ​​of the lengths and of the sides: ").split()))
        print(f"The area of ​​a rectangle is {area_rectangle(a, b)}")
    case "2":
        a, h = list(map(int, input("Enter the values ​​of the length and height: ").split()))
        print(f"The area of ​​a triangle is {area_triangle(a, h)}")
    case "3":
        r = int(input("Enter the radius values: "))
        print(f"The area of ​​a circle is {area_circle(r)}")
    case _:
        print("Wrong variant!!!")  






  