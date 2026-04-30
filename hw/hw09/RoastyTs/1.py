import random

numbertoguess = random.randint(1,100)
print(numbertoguess)
print("Welcome to the Guess The Number game. You need guess the number from 1 to 100 to win the game in 10 attempts. We will give you hints.")
x=0
while x < 10:
    userguess=int(input("Enter the number:"))
    if userguess == numbertoguess:
        print("Congrats!!! You guessed the number!")
        print(f"Nice work. You guessed it on Attempt {x+1}")
        break
    elif userguess > numbertoguess:
        print(f"Attempt {x+1}. The number you printed is more than my")
        x+=1
    elif userguess < numbertoguess:
        print(f"Attempt {x+1}.The number you printed is less than my")
        x+=1
    elif userguess > 100 or userguess < 0:
        print("The number might be from 1 to 100") 
if x == 10:
    print("GAME OVER")
