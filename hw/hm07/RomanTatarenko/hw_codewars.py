import math


# Jenny's secret message
# =====================================
# Jenny has written a function that returns a greeting for a user.
# However, she's in love with Johnny, and would like to greet him slightly
# different. She added a special case to her function, but she made a mistake.
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# Find The Distance Between Two Points
# =====================================
# Given two ordered pairs calculate the distance between them.
# Round to two decimal places. This should be easy to do in 0(1) timing.
def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


# No yelling!
# =====================================
# Write a function taking in a string like
# WOW this is REALLY  amazing and returning Wow this is really amazing.
# String should be capitalized and properly spaced.
def filter_words(st):
    cleaned_words = ""
    words = st.split(' ')
    for word in words:
        if word:
            cleaned_words += f"{word} "

    return cleaned_words.capitalize().rstrip()


# Convert a Number to a String
# =====================================
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
def number_to_string(num):
    num = str(num)
    return num


# Reversing Words in a String
# =====================================
# You need to write a function that reverses the words in a given string.
# Words are always separated by a single space.
# As the input may have trailing spaces, you will also need to ignore
# unneccesary whitespace.
# Example (Input --> Output)
def reverse(st):
    words = st.strip().split()
    if len(words) == 1:
        return words[0]

    first_word = words[0]
    reduce_words = words[1:]
    result = reverse(" ".join(reduce_words)) + f' {first_word}'
    return result


# Reverse List Order
# =====================================
# In this kata you will create a function that takes in a list
# and returns a list with the reverse order.
def reverse_list(l):
    l.reverse()
    return l


# Multiples of 3 or 5
# =====================================
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples
# of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.
# Note: If a number is a multiple of both 3 and 5, only count it once.
# Courtesy of projecteuler.net (Problem 1)
def solution(number):
    if number < 0:
        return 0

    result = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


# Will you make it?
# =====================================
# You were camping with your friends far away from home,
# but when it's time to go back, you realize that your fuel is running out
# and the nearest pump is 50 miles away! You know that on average,
# your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it
# is possible to get to the pump or not.
# Function should return true if it is possible and false if not.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    required_fuel = distance_to_pump / mpg
    return True if required_fuel <= fuel_left else False


# Are You Playing Banjo?
# =====================================
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r",
# you are playing banjo!
# The function takes a name as its only argument,
# and returns one of the following strings:
def are_you_playing_banjo(name):
    return (
        f"{name} plays banjo"
        if name.lower().startswith('r')
        else f"{name} does not play banjo"
    )


# Convert boolean values to strings 'Yes' or 'No'
# =====================================
# Complete the method that takes a boolean value and return
# a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'


# Counting sheep
# =====================================
# Consider an array/list of sheep where some sheep may be missing
# from their place. We need a function that counts the number of sheep
# present in the array (true means present).
def count_sheeps(sheep):
    return sheep.count(True)


# Is this my tail?
# =====================================
def correct_tail(body, tail):
    return body.endswith(tail)
