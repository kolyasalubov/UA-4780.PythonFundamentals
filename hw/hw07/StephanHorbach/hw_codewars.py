# I. Jenny's secret message
def greet(name):
    return f"Hello, {name}!" if name != "Johnny" else "Hello, my love!"

print(greet("Johnny"))

# II. Find The Distance Between Two Points'
def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

print(distance(1, 1, 2, 2))

# III. No yelling!
def filter_words(text):
    return ' '.join(text.capitalize().split())

# IV. Convert a Number to a String
def number_to_string(num):
    return str(num)

# V. Reversing Words in a String
def reverse(text):
    return ' '.join(text.split()[::-1])

# VI. Reverse List Order
def reverse_list(lst):
    return lst[::-1]

# VII. Multiples of 3 or 5
def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith("r") else f"{name} does not play banjo"

# X. Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# XI. Counting sheep
def count_sheep(sheep):
    return sum(1 for s in sheep if s)

# XII. Is this my tail?
def check_tail(body, tail):
    return body.endswith(tail)
