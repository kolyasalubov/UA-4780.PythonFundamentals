from random import randint

guess_number = randint(1, 100)
for attempt in range(10):
    user_guess = int(input("Please guess a number: "))
    if user_guess == guess_number:
        print("Congratulations! You guessed the number.")
        break

    if user_guess < guess_number:
        print("Your guess is too low.")

    if user_guess > guess_number:
        print("Your guess is too high.")

    if attempt == 9:
        print("Sorry, you didn't guess the number.")
