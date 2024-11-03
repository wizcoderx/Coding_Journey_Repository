'''
   Define a class `Employee` with attributes `name`, `position`, and `salary`. Create a `Department` class that stores multiple employees and has methods to add an employee, remove an employee, calculate the average salary in the department, and list all employees.
'''
#The below is the Employee Class
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

#The below is the Department Class
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    #Method to add an employee
    def add_employee(self, employee):
        self.employees.append(employee)

    #Method to remove and employee
    def remove_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                return f"{name} has been removed from the department"
        return f"No employee with name {name} found in the department"

    #Mehtod to Calculate the average salary in the department and list all the employees
    def calculate_average_salary(self):
        if len(self.employees) == 0:
            return "No employees in the department"
        else:
            total_salary = sum(employee.salary for employee in self.employees)
            average_salary = total_salary / len(self.employees)
            return f"Average salary in the department is {average_salary} and the employees are: {', '.join(employee.name for employee in self.employees)}"

# Creating Employee instances
employee1 = Employee("Alice", "Manager", 75000)
employee2 = Employee("Bob", "Developer", 60000)
employee3 = Employee("Charlie", "Designer", 55000)

# Creating a Department instance
department = Department("Engineering")

# Adding employees to the department
department.add_employee(employee1)
department.add_employee(employee2)
department.add_employee(employee3)

# Displaying average salary and employees in the department
print(department.calculate_average_salary())

# Removing an employee
print(department.remove_employee("Bob"))

# Displaying average salary and employees after removal
print(department.calculate_average_salary())

# Attempting to remove an employee not in the department
print(department.remove_employee("Diana"))
