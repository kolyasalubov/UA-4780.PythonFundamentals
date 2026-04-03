

###
print("\nEX_1\n")
###


"""
Task1. Create a polygon class and a rectangle class 
that inherits from the polygon class and finds the square 
of rectangle.
"""


class Polygon:
    
    def __init__(self, *args):        
        self.sides = args

    
class Rectangle(Polygon):

    def __init__(self, *args):
        super().__init__(*args)
        self.a = args[0]
        self.b = args[1]
        
    def area_rectangle(self):
        result = self.a * self.b
        return  int(result) if result % 1 == 0 else result
    
    def show_rec_area(self):
        return f"Area of the rectangle is {self.area_rectangle()}"
        
    
rec_1 = Rectangle(9, 3)
print(rec_1.show_rec_area())












