class Employee:
    """
    Represents an employee with a name and salary.
    Provides functionality to increase salary and display employee information.
    """
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def increase_salary(self, percent):
        """
        Increases the employee's salary by a given percentage.
        
        Args:
            percent (float): The percentage increase to apply.
        """
        self._salary += self._salary * percent / 100

    def display_info(self):
        """
        Displays the employee's name and current salary.
        """
        print(f"Employee: {self._name}, Salary: ₹{self._salary:.2f}")


# Take input from user
try:
    name = input("Enter employee name: ")
    salary = float(input("Enter current salary: "))
    percent = float(input("Enter percentage increase: "))

    emp = Employee(name, salary)
    emp.increase_salary(percent)
    emp.display_info()

except ValueError:
    print("Invalid input. Please enter numeric values for salary and percentage.")