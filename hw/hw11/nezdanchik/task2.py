def get_day(num: int):
    if num <= 0 or num > 7:
        raise IndexError
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[(num - 1) % 7]


if __name__ == '__main__':
    while True:
        try:
            input_day = int(input("Enter a number:"))
            print("The day is:", get_day(input_day))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("Invalid input. The number must be between 1 and 7.")
