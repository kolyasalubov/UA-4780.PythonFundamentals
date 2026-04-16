def process_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним числом!")
    
    if age % 2 == 0:
        return "парний"
    else:
        return "непарний"

try:
    user_input = int(input("Введіть свій вік: "))
    result = process_age(user_input)
    print(f"Ваш вік — {result}.")
except ValueError as e:
    print(f"Помилка: {e}")