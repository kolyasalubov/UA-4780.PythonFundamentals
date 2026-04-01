import random
secret_number = random.randint(1, 100)
print("Я загадав число від 1 до 100. Спробуй вгадати!")

attempts = 10
while True:
    gues = int(input("Твій варіант: "))
    attempts -= 1  
    
    if gues < secret_number:
        print("Неправильно, моє число більше")
        print(f"Залишилось спроб: {attempts}")
    elif gues > secret_number:
        print("Неправильно, моє число менше")
        print(f"Залишилось спроб: {attempts}")
    else:
        print("Вірно! Ти вгадав!")
        break
    if attempts == 0:
        print(f"Ти програв! Спроби закінчились. Я загадав число: {secret_number}")
        break
    