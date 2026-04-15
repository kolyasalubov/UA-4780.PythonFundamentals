

"""
EX_2
Write a program that analyzes the entered number and, depending on the number, gives 
the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take 
into account cases of entering numbers from 8 and more, as well as cases of entering non
numerical data.
"""


class DayError(Exception):
    pass


def check_day(day):
    if not day:
        raise DayError("Please enter your day")
    day = int(day)
    if day <= 0:
        raise DayError("Incorrect day (must be 1-7)")     
    if day > 7:
        raise DayError("Please enter a realistic day (1-7)")    
    return day

def main():

    while True:

        day = input("Enter number of your day: ").replace(" ", "")

        days = ["Monday", "Tuesday", 
                "Wednesday", "Thursday", 
                "Friday", "Saturday", 
                "Sunday"]

        try:
            day = check_day(day)            
        except ValueError:
            print("Input error! Only numbers!")    
        except DayError as ae:
            print(ae)     
        else:         
            return days[day - 1]
        
if __name__ == "__main__":
    print(main())



