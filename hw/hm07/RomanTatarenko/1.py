from typing import Union


def get_max_of_two(x: Union[int, float], y: Union[int, float]
                   ) -> Union[int, float]:
    """
    Returns the larger of two numbers.

    :param x: first number (int or float)
    :param y: second number (int or float)
    :return: the larger number between x and y
    """
    return x if x > y else y
