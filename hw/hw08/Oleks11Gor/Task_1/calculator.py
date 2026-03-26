

"""
EX_1
Create a module with functions of addition, subtraction, 
multiplication, division. And in another module - calculator.py, it is 
necessary to ask the user what action he wants to perform and 
with what numbers and perform the necessary actions.
"""

import module

def calculate_action(num1, act, num2):
    match action:
        case "+":
            result = module.add(number_1, number_2)
            
        case "-":
            result = module.sub(number_1, number_2)
            
        case "*":
            result = module.mult(number_1, number_2)
            
        case "/":
            if number_2 == 0:
                result = "Error: Division by zero!!!"
            else:    
                result = module.div(number_1, number_2)
            
        case _:
            result = "Error: Wrong action!!!"

    if isinstance(result, (int, float)):
        return int(result) if result.is_integer() else result
    else:
        return result



if __name__ == "__main__":
    number_1 = float(input("Enter the first number: "))
    action = input("Choose the action (+, -, *, /): ")
    number_2 = float(input("Enter the second number: "))

    result = calculate_action(number_1, action, number_2)

    print(f"Result: {result}")











