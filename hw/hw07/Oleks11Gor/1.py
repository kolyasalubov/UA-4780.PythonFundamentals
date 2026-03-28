

###
print("\nEX_1")
###

"""
Task1. Write a function that returns the largest number of two 
numbers 
(use DocStrings documentation strings in the function).
"""

def bigger_num(x):
    """
    This function returns the largest value.
    
    Args: x (list): A list containing exactly two numbers, 
    provided by the user for comparison.
       
    Returns: the maximum  numbers in the list.   
    """
    return max(x)
    
num = list(map(int, input("Enter the values: ").split()))
print(bigger_num(num))

