# Task 3
def count_characters(s):
    """
    Counts the occurrences of each character in a string.

    Args:
        s (str): Input string.

    Returns:
        dict: A dictionary mapping each character to its count.
    """
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result


print(count_characters("hello"))
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}