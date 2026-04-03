

###
print("\nEX_3\n")
###


"""
Task3. Create an employee class. Each employee has characteristics such as name
and salary. The class should have a counter that calculates the total number of
employees, as well as a method that prints the total number of employees and a
method that displays information about each employee in particular, namely the
nameandsalary.
In addition to creating a class, display information about the base classes from which 
the employee class is inherited (__base__), the class namespace (__dict__), the 
class name (__name__), the module name in which the class is defined 
(__module__), the documentation bar ( __doc__)
"""


class Employee:

    """
    Employee class, where each employee has characteristics such as name
    and salary
    """

    total_num_emp = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_num_emp += 1

    @classmethod
    def get_total_emp(cls):
        return f"Total number of employees: {cls.total_num_emp}"

    def get_info_emp(self):
        return f"{self.name}: {self.salary}"
    

emp_1 = Employee("Zack", 10000)
emp_2 = Employee("Ben", 15000)

print(emp_1.get_info_emp())
print(emp_2.get_info_emp())
print(Employee.get_total_emp())

print(emp_1.get_total_emp())
print(emp_1.get_total_emp())

print("\n")

print(Employee.__base__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)

for key, value in Employee.__dict__.items():
    print(f"{key} : {value}")

