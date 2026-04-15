#hw07 task3

def count_chars(string: str) -> dict:
    """
    Counts the occurrence of each character in a given string and returns
    the results as a dictionary.

    :param string: The string for which character count is to be calculated.
    :return: A dictionary with characters as keys and their counts as values.
    """
    result = {}

    for char in string:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    return result


if __name__ == '__main__':
    string = input("Enter a string: ").strip()
    print("Result: ", count_chars(string))
