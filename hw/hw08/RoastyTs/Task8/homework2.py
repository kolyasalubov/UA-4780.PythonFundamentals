import pack1


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
        area = pack1.recarea(width,length)
        print(f"Area of rectangle is {area} cm")
    case 2:
        print("Enter height of triangle (in cm)")
        h = int(input())
        print("Enter base of triangle (in cm)")
        b = int(input())
        area = pack1.triarea(h,b)
        print(f"Area of triangle is {area} cm")
    case 3:
        print("Enter radius of circle (in cm)")
        r = int(input())
        area = pack1.circarea(r)
        print(f"Area of circle is {area} cm")


