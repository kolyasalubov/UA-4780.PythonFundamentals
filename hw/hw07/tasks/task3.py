def count_chars(string: str) -> dict:
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