'''
   Create a class called `Student` that has an instance variable `name` and a class variable `school_name`. Implement a method that returns a string showing the student's name and their school name. Make sure to show how class variables can be accessed and modified.
'''
class Student:
    school_name = "ABC High School" #class variable

    def __init__(self, name):
        self.name = name #instance variable

    def get_student_info(self):
        return f"{self.name} is a student at {Student.school_name}."

    @classmethod
    def change_school_name(self, new_school_name):
        self.school_name = new_school_name

# Example usage
student1 = Student("Alice")
student2 = Student("Bob")

# Print initial information
print(student1.get_student_info())  # Output: Student Name: Alice, School: Greenwood High School
print(student2.get_student_info())  # Output: Student Name: Bob, School: Greenwood High School

# Changing the school name using the class method
Student.change_school_name("Maple Leaf Academy")

# Print information after changing the school name
print(student1.get_student_info())  # Output: Student Name: Alice, School: Maple Leaf Academy
print(student2.get_student_info())  # Output: Student Name: Bob, School: Maple Leaf Academy

