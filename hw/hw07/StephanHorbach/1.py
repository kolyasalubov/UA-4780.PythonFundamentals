# Task 1
def get_largest(a, b):
    """
    Returns the largest of two numbers.

    Args:
        a (int | float): First number.
        b (int | float): Second number.

    Returns:
        int | float: The larger of the two numbers.
    """
    return a if a >= b else b


print(get_largest(10, 20))  # 20
print(get_largest(5, 3))    # 5