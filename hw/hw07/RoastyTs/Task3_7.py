def countw(word):
    a = {}
    for x in word:            
        a.update({x : word.count(x)})
    return a

print("Enter word or phrase to calculate number of characters")
userinp = str(input())
print(countw(userinp))