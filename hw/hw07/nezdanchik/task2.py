#hw07 task2

import math


def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle using its length and width.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The area of the rectangle.
    """
    return round((length * width), 2)


def calculate_triangle_area(base: float, height: float) -> float:
    """
    Calculate the area of a triangle using its base and height.

    :param base: The length of the base of the triangle.
    :param height: The height of the triangle.
    :return: The area of the triangle.
    """
    return round((0.5 * base * height), 2)


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle based on the given radius.

    :param radius: The radius of the circle.
    :return: The area of the circle with the given radius.
    """
    return round((math.pi * radius ** 2), 2)


if __name__ == "__main__":
    print("Calculate area for:\n1.Rectangle\n2.Triangle\n3.Circle")

    while True:
        choice = input("Enter your choice (1,2,3): ").strip()

        match choice:
            case "1":
                length, width = map(float, input("Enter a length and width (separated by space): ").strip().split())
                print("The area is:", calculate_rectangle_area(length, width))
                break
            case "2":
                base, height = map(float, input("Enter a base and height (separated by space): ").strip().split())
                print("The area is:", calculate_triangle_area(base, height))
                break
            case "3":
                radius = float(input("Enter a radius: "))
                print("The area is:", calculate_circle_area(radius))
                break
            case _:
                print("Invalid choice")
