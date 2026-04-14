from typing import Union


def calc_triangle_area(base: Union[int, float], height: Union[int, float]
                       ) -> Union[int, float]:
    """
    Calculates the area of a triangle using its base and height.

    :param base: the length of the base of the triangle (int or float)
    :param height: the height of the triangle perpendicular to the base
                    (int or float)
    :return: the area of the triangle
    """
    return round(1 / 2 * base * height, 2)


def calc_rectangle_area(a: Union[int, float], b: Union[int, float]
                        ) -> Union[int, float]:
    """
    Calculates the area of a rectangle.

    :param a: the length of one side of the rectangle (int or float)
    :param b: the length of the other side of the rectangle (int or float)
    :return: the area of the rectangle
    """
    return round(a * b, 2)


def calc_circle_area(radius: Union[int, float]) -> Union[int, float]:
    """
    Calculates the area of a circle using its radius.

    :param radius: the radius of the circle (int or float)
    :return: the area of the circle
    """
    pi = 3.141592653589793
    return round(pi * radius ** 2, 2)


def main():
    user_choice = input(
        "Choose a shape to calculate its area:"
        "\n1 - triangle; \n2 - square; \n3 - circle"
        "\nPlease enter your digit: "
    )
    try:
        user_choice = int(user_choice)
    except ValueError:
        raise ValueError("Invalid input. Please enter a number (1, 2, or 3).")

    match user_choice:
        case 1:
            print("You selected triangle.")

            try:
                base = float(
                    input("Please enter the base of the triangle: ")
                )

                height = float(
                    input("Please enter the height of the triangle: ")
                )
            except ValueError:
                raise ValueError(
                    "Invalid input. Base and height must be numbers."
                )

            result = calc_triangle_area(base, height)
            print(f"The area of the triangle is {result}")

        case 2:
            print("You selected rectangle.")

            try:
                a = float(
                    input("Please enter the side 'a' of the rectangle: ")
                )

                b = float(
                    input("Please enter the side 'b' of the rectangle: ")
                )
            except ValueError:
                raise ValueError(
                    "Invalid input. Sides of the rectangle must be numbers."
                )

            result = calc_rectangle_area(a, b)
            print(f"The area of the rectangle is {result}")

        case 3:
            print("You selected circle.")

            try:
                radius = float(
                    input("Please enter the radius of the circle: ")
                )
            except ValueError:
                raise ValueError(
                    "Invalid input. Radius of the circle must be number."
                )
            result = calc_circle_area(radius)
            print(f"The area of the circle is {result}")

        case _:
            raise ValueError("Invalid choice. Please select 1, 2, or 3.")
