from random import randint

number = randint(1,100)
attempt = 0

while attempt < 10:
    atmp = int(input())
    attempt += 1
    if number == atmp:
        print('Вгадав')
        break
    elif number < atmp:
        print('Менше')
    else:
        print("Більше")
if attempt == 10:
    print('Всі спроби вичерпано - ти програв')