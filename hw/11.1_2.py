def get_day_of_week():
    days = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П'ятниця",
        6: "Субота",
        7: "Неділя"
    }

    try:
        user_input = input("Введіть номер дня тижня (1-7): ")
        number = int(user_input)

        if number in days:
            print(f"Це {days[number]}.")
        else:
            print("Помилка: введіть число саме від 1 до 7.")
            
    except ValueError:
        print("Помилка: ви ввели не числові дані.")

get_day_of_week()