def calculate_chars(value: str) -> dict:
    """
    Counts the occurrences of each character in a string.

    :param value: the input string
    :return: a dictionary where keys are characters and values are their counts
    """
    result = {}
    for char in value:
        result.update({char: value.count(char)})
    return result
