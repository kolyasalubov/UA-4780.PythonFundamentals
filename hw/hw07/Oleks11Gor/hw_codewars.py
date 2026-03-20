

# I. Jenny's secret message

def greet(name):
    
    # if name == "Johnny":
    #     return "Hello, my love!"
    # return "Hello, {name}!".format(name=name)    
    
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"



# II. Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)



# III. No yelling!

def filter_words(st):
    return " ".join(st.capitalize().split())



# IV. Convert a Number to a String

def number_to_string(num):
    return str(num)


# V. Reversing Words in a String

def reverse(st):
    return " ".join(reversed(st.split()))


# VI. Reverse List Order

def reverse_list(l):
    return list(reversed(l))


# VII. Multiples of 3 or 5

def solution(number):
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])


# VIII. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * fuel_left >= distance_to_pump else False 


# IX. Are You Playing Banjo?

def are_you_playing_banjo(name):
    return name + " plays banjo" if name[0] in ["R", "r"] else name + " does not play banjo"


# X. Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# XI. Counting sheep

def count_sheeps(sheep):
    return sum([x for x in sheep if x])


# XII. Is this my tail?

def correct_tail(body, tail):
    return tail == body[-1]
    

