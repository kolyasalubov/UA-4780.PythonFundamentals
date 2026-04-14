class Polygon:
    def __init__(self, no_of_sides: int):
        self.no_of_sides = no_of_sides
        self.sides = []

    def add_sides(self):
        self.sides = [float(input(f"Enter side ({no+1}): ")) for no in range(self.no_of_sides)]

    def __repr__(self):
        return f"Polygon with {self.no_of_sides} sides: {self.sides}"


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)

    def square(self):
        if len(self.sides) < 2:
            raise ValueError("Not enough sides to calculate square")

        return self.sides[0] * self.sides[1]


if __name__ == "__main__":
    rectangle = Rectangle()
    rectangle.add_sides()
    print(rectangle.square())
