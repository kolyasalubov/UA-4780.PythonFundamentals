import math

# https://www.codewars.com/kata/55225023e1be1ec8bc000390

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"

    return f"Hello, {name}!"

# https://www.codewars.com/kata/simple-find-the-distance-between-two-points

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    return round((math.sqrt(dx ** 2 + dy ** 2)), 2)

# https://www.codewars.com/kata/no-yelling

def filter_words(st):
    return " ".join(st.strip().split()).capitalize()

# https://www.codewars.com/kata/convert-a-number-to-a-string

def number_to_string(num):
    return str(num)

# https://www.codewars.com/kata/reversing-words-in-a-string

def reverse(st):
    return " ".join(st.split()[::-1])

# https://www.codewars.com/kata/reverse-list-order

def reverse_list(l):
    return l[::-1]

# https://www.codewars.com/kata/multiples-of-3-or-5

def solution(number):
    result = 0

    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            result += num

    return result

# https://www.codewars.com/kata/will-you-make-it

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

#https://www.codewars.com/kata/are-you-playing-banjo

def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"

    return name + " does not play banjo"

# https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python

def count_sheeps(sheep):
  return sheep.count(True)

# https://www.codewars.com/kata/is-this-my-tail/train/python

def correct_tail(body, tail):
    return body[-1] == tail
