

# I. Ball-super-ball


class Ball(object):
    
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type


# II. Color-ghost


class Ghost(object):
    
    colors = {"white", "yellow", "purple", "red"}
    
    def __init__(self):        
        self.color = Ghost.colors.pop()
        Ghost.colors.add(self.color)


# III. Basic-subclasses-Adam-and-Eve


class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():    
    result = [Man(), Woman()]
    return result


# IV. Classy-classes


class Person:
    
    def __init__(self,name="john",age=34):
        self.name = name
        self.age = age
        self.info=f"{name}s age is {age}"


# V. Building Spheres


import math


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        area = 4 * math.pi * (self.radius ** 2)
        return round(area, 5)

    def get_density(self):
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        density = self.mass / volume
        return round(density, 5)
    

# VI. Dynamic Classes


import re

def class_name_changer(cls, new_name):    
    pattern = r"^[A-Z][a-zA-Z0-9]*$"    
    if not re.match(pattern, new_name):
        raise Exception("Invalid name!")
    cls.__name__ = new_name


