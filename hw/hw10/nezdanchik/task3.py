class Employee:
    """
    Represents an employee with a name and a salary. Manages the total count
    of employees and provides access to employee information.

    The Employee class is designed to encapsulate the details of an employee,
    including their name and salary. It maintains a class-level count of the
    number of employees instantiated and provides class and instance methods
    to retrieve relevant employee information.

    :ivar no_employees: Static counter that keeps track of the total number of
        employee instances created.
    :type no_employees: int
    """
    no_employees = 0

    def __init__(self, name, salary):
        Employee.no_employees += 1
        self.__name = name
        self.__salary = salary

    @classmethod
    def total_employees(cls):
        return cls.no_employees

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    def employee_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"


if __name__ == "__main__":
    employee = Employee("John", 50000)
    print(employee.employee_info())
    print(f"No of employees: {Employee.total_employees()}")
    print(Employee.__bases__)
    print(Employee.__dict__)
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__doc__)
