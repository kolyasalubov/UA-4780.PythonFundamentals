import math
import random

# https://www.codewars.com/kata/regular-ball-super-ball
class Ball:
    def __init__(self, ball_type: str = "regular"):
        self.ball_type = ball_type

# https://www.codewars.com/kata/color-ghost
class Ghost:
    colors = ["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = random.choice(Ghost.colors)

# https://www.codewars.com/kata/basic-subclasses-adam-and-eve
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    m = Man()
    w = Woman()
    return [m, w]

# https://www.codewars.com/kata/classy-classes
class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @property
    def info(self):
        return f"{self.__name}s age is {self.__age}"

# https://www.codewars.com/kata/55c1d030da313ed05100005d
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self, rounded: bool = True):
        volume = (4/3) * math.pi * math.pow(self.radius, 3)
        if rounded:
            return round(volume, 5)
        return volume

    def get_surface_area(self):
        return round(4 * math.pi * math.pow(self.radius, 2), 5)

    def get_density(self):
        return round(self.mass / self.get_volume(rounded=False), 5)

# https://www.codewars.com/kata/55ddb0ea5a133623b6000043
def class_name_changer(cls, new_name: str):
    if new_name.isalnum() and new_name[0].isupper():
        cls.__name__ = new_name
    else:
        raise ValueError("Invalid class name")
