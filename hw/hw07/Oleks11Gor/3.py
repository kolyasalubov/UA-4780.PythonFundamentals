

###
print("\nEX_3")
###

"""
Task3. Write a function that calculates the number of characters 
included in a given string
• input: "hello"
• output: {"h":1, "e":1,"l":2,"o":1}

"""

def co_char(val):    
    d = {}
    g = []
    for i in val:
        if i not in g:
            g.append(i)
            n = val.count(i)
            d.update({i:n})
    return d

text = tuple(input("Enter your str: "))

print(co_char(text))

## or

def co_char(val):    
    d = {}
    for i in val:
        if i not in d:            
            d[i] = 1
        else:    
            d[i] += 1
    return d

text = input("Enter your str: ")

print(co_char(text))

## or

text = input("Enter your str: ")

print((lambda val: {i: val.count(i) for i in set(val)})(text))



