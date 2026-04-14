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
    return round((math.pi * math.pow(radius,2)), 2)
