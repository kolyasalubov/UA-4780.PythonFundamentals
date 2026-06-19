class Employee:
    
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def display_count(cls):
        print(f"Загальна кількість співробітників: {cls.counter}")

    def display_info(self):
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")

emp1 = Employee("Олексій", 50000)
emp2 = Employee("Марія", 60000)

emp1.display_info()
Employee.display_count()

print("\n--- Метадані класу ---")
print(f"Базові класи: {Employee.__bases__}")
print(f"Простір імен: {Employee.__dict__}")
print(f"Назва класу: {Employee.__name__}")
print(f"Назва модуля: {Employee.__module__}")
print(f"Документація: {Employee.__doc__}")