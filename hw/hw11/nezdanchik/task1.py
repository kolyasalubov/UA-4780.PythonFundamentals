class AgeError(Exception):
    pass

def is_odd(n):
    if n < 0:
        raise AgeError("Age must be a positive number.")

    return n % 2 != 0


if __name__ == "__main__":
    while True:
        try:
            age = int(input("Enter your age: "))
            if is_odd(age):
                print("Your age is odd")
                break
            else:
                print("Your age is even")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
        except AgeError as e:
            print(e)
