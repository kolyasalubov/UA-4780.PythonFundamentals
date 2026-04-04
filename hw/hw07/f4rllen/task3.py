def count_characters(string):
    return {char: string.count(char) for char in string}

print(count_characters("hello"))