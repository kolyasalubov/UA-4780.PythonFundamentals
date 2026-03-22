from arealib import calculate_rectangle_area, calculate_triangle_area, calculate_circle_area


if __name__ == "__main__":
    print("Calculate area for:\n1.Rectangle\n2.Triangle\n3.Circle")

    while True:
        choice = input("Enter your choice (1,2,3): ").strip()

        match choice:
            case "1":
                length, width = map(float, input("Enter a length and width (separated by space): ").strip().split())
                print("The area is:", calculate_rectangle_area(length, width))
                break
            case "2":
                base, height = map(float, input("Enter a base and height (separated by space): ").strip().split())
                print("The area is:", calculate_triangle_area(base, height))
                break
            case "3":
                radius = float(input("Enter a radius: "))
                print("The area is:", calculate_circle_area(radius))
                break
            case _:
                print("Invalid choice")
