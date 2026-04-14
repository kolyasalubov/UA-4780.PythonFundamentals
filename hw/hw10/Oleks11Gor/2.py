

###
print("\nEX_2\n")
###


"""
Task2. Create a class Human, everyone has a name, create a method in the 
class that displays a welcome message to each person. Create a class method 
in the class that returns information that it is a species of "Homosapiens". And
in the class create a static method that returns an arbitrary message.
"""


class Human:

    def __init__(self, name):        
        self.name = name
                
    def welcome_message(self):        
        return  f"Hello, {self.name}"
    
    @classmethod
    def information(cls):
        return f"It is a species of \"Homosapiens\""
    
    @staticmethod
    def arbitrary_message():
        return f"\"Homosapiens\" is a {Human.__name__}"


person_1 = Human("Robert")

print(person_1.welcome_message())
print(Human.welcome_message(person_1))

print(person_1.information())
print(Human.information())

print(person_1.arbitrary_message())
print(Human.arbitrary_message())



