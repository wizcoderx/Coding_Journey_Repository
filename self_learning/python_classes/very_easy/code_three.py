'''
Question 3: Student Grades
Create a Student class with:

An __init__ method that takes name and grades (a list of integers) as parameters.
A get_average method that returns the average of the grades.
A display_info method that prints the students name and average grade.
'''

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    #Average method
    def get_average(self):
        return sum(self.grades) / len(self.grades) 

    #Display info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Average Grade: {self.get_average()}")

student = Student("Alice", [80, 90, 100])
print(student.get_average())  # Output: 90.0
student.display_info()        # Output: "Alice - Average Grade: 90.0"
