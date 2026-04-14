

"""
EX_1
Write a program that prompts the user to enter their age, and then displays a 
message stating whether the age is even or odd. The program must provide the ability 
to enter a negative number, and in this case generate an exception. The master code 
should call a function that processes the information entered.
"""


class AgeError(Exception):
    pass


def check_age(age):

    if not age:
        raise AgeError("Please enter your age")
          
    age = int(age)

    if age <= 0:
        raise AgeError("Incorrect age")     
    if age > 135:
        raise AgeError("Please enter a realistic age")
    
    return age
        

def main():

    while True:

        age = input("Enter your age: ").replace(" ", "")

        try:
            age = check_age(age)
            
        except ValueError:
            print("Input error! Only numbers!")    
        except AgeError as ae:
            print(ae)     
        else:
            if age % 2 == 0:
                return "Your age is even"        
            return "Your age is odd"

if __name__ == "__main__":    
    print(main())















