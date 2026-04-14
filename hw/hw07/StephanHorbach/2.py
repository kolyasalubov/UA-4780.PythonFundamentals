# Task 2
def rectangle_area(width, height):
    return width * height


def triangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return 3.14159 * radius ** 2


def main():
    print("Choose a shape:")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")

    choice = input("Your choice: ")

    if choice == "1":
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        print(f"Rectangle area: {rectangle_area(w, h)}")

    elif choice == "2":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Triangle area: {triangle_area(b, h)}")

    elif choice == "3":
        r = float(input("Enter radius: "))
        print(f"Circle area: {circle_area(r):.4f}")

    else:
        print("Invalid choice.")


main()