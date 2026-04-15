#Jenny
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {0}!".format(name)
######################################
#Distance
import math

def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(d, 2)

print(distance(0, 0, 3, 4))
#######################################
#No yelling!
def filter_words(st):
    return " ".join(st.strip().split()).capitalize()
#######################################
#Convert a Number to a String
def number_to_string(num):
    return str(num)
#######################################
#Reversing Words in a String
def reverse(st):
    return " ".join(st.split()[::-1])
#######################################
#Reverse List Order
def reverse_list(l):
    return l[::-1]
#######################################
#Multiples of 3 or 5
def solution(number):
    result = 0

    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            result += num

    return result
#######################################
#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * fuel_left >= distance_to_pump else False 
#######################################
#Are You Playing Banjo?
def are_you_playing_banjo(name):
    return name + " plays banjo" if name[0] in ["R", "r"] else name + " does not play banjo"
#######################################
#Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return "Yes" if boolean else "No"
#######################################
#Counting sheep
def count_sheeps(sheep):
    return sum([x for x in sheep if x])
#######################################
#Is this my tail?
def correct_tail(body, tail):
    return tail == body[-1]
