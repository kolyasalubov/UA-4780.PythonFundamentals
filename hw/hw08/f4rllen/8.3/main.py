import geometry

figure = input("Яку фігуру рахуємо? (1-прямокутник, 2-трикутник, 3-коло): ")

if figure == '1':
    print("Площа:", geometry.rectangle_area(float(input("a: ")), float(input("b: "))))
elif figure == '2':
    print("Площа:", geometry.triangle_area(float(input("h: ")), float(input("a: "))))
elif figure == '3':
    print("Площа:", geometry.circle_area(float(input("r: "))))