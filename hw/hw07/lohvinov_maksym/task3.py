def count_characters(text):
    result = {}
    for letter in text:
        if letter in result:
            result[letter] = result[letter] + 1
        else:
            result[letter] = 1
    return result
    
print(count_characters("hello"))
    