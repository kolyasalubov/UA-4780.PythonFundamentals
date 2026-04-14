def recarea(width = 1, length = 1):
    area = width * length
    return area
def triarea(height = 1, base = 2):
    area = 0.5 * height * base
    return area
def circarea(radius = 1):
    area = 3.14 * radius**2
    return area

print("Hi, I am area calculator. Area of what figure do you want calculate?")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")
x = int(input())
match x:
    case 1:
        print("Enter width of rectangle (in cm)")
        width = int(input())
        print("Enter length of rectangle (in cm)")
        length = int(input())
        area = recarea(width,length)
        print(f"Area of rectangle is {area} cm")
    case 2:
        print("Enter height of triangle (in cm)")
        h = int(input())
        print("Enter base of triangle (in cm)")
        b = int(input())
        area = triarea(h,b)
        print(f"Area of triangle is {area} cm")
    case 3:
        print("Enter radius of circle (in cm)")
        r = int(input())
        area = circarea(r)
        print(f"Area of circle is {area} cm")
