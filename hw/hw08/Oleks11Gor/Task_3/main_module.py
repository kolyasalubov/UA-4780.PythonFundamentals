

"""
EX_3
Write a program that calculates the area of a rectangle S=a*b, the area of a 
triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in 
another module in which we ask the user the area of which figure he wants to 
calculate.
(To perform the task, you need to import the math module, and from it the
pow() function and the value of the variable pi, and module, which contains
three functions for finding areas, into the main program. The basic logic of the
program is executed in the main module).
"""

from func_module import area_rectangle, area_triangle, area_circle
from math import pow, pi

def get_area(fig):
    match fig:
        case "1":
            a, b = list(map(float, input("Enter the values ​​of the lengths and of the sides (space separated): ").split()))
            result = area_rectangle(a, b)
        case "2":
            a, h = list(map(float, input("Enter the values ​​of the length and height (space separated): ").split()))
            result = area_triangle(a, h)
        case "3":
            r = float(input("Enter the radius values: "))
            result = area_circle(r, pi, pow)
        case _:
            result = "Wrong variant!!!"
    return result



if __name__ == "__main__":
    var_of_fig = input("Choose your figure (1 - rectangle, 2 - triangle, 3 - circle): ")

    result = get_area(var_of_fig)
    print(f"Result: {result}")

    




