import math

# 1. Jenny
greet = lambda name: f"Hello, {'my love' if name == 'Johnny' else name}!"

# 2. Distance
distance = lambda x1, y1, x2, y2: round(math.dist((x1, y1), (x2, y2)), 2)

# 3. No yelling!
filter_words = lambda st: " ".join(st.split()).capitalize()

# 4. Convert a Number to a String
number_to_string = lambda num: str(num)

# 5. Reversing Words in a String
reverse = lambda st: " ".join(st.split()[::-1])

# 6. Reverse List Order
reverse_list = lambda l: l[::-1]

# 7. Multiples of 3 or 5
solution = lambda n: sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

# 8. Will you make it?
zero_fuel = lambda d, mpg, f: mpg * f >= d

# 9. Are You Playing Banjo?
are_you_playing_banjo = lambda n: f"{n} {'plays' if n[0].lower() == 'r' else 'does not play'} banjo"

# 10. Convert boolean values to strings
bool_to_word = lambda b: "Yes" if b else "No"

# 11. Counting sheep
count_sheeps = lambda s: s.count(True)

# 12. Is this my tail?
correct_tail = lambda b, t: b.endswith(t)