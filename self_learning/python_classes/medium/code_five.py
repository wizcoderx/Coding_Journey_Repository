'''
	Update the `Student` class to have a dictionary attribute `grades`, where keys are subject names and values are grades. Add methods `add_grade(subject, grade)` to add a grade and `average_grade` to calculate the average grade across subjects. Add a class method `change_school_name` to modify the class variable `school_name`.
'''

class Student:

	school_name = "ABC High School" #class variable

	def __init__(self, name):
		self.name = name #instance variable
		self.grades = {} #instance variable #keys are subject name and values are grades

	def get_student_info(self):
		return f"{self.name} is a student at {Student.school_name}."

	@classmethod
	def change_school_name(cls, new_school_name):
		cls.school_name = new_school_name
		return f"School name changed to {cls.school_name}."

	def add_grade(self, subject, grade):
		self.grades[subject] = grade
		return f"Grade added for {subject} with grade {grade}."

	def average_grade(self):
		if not self.grades:
			return "No grades available."
		return sum(self.grades.values()) / len(self.grades)

# Create a student
student1 = Student("Alice")

# Add some grades
student1.add_grade("Math", 85)
student1.add_grade("English", 92)
student1.add_grade("Science", 78)

# Get student info
print(student1.get_student_info())  # Output: Alice is a student at ABC High School.

# Calculate average grade
average = student1.average_grade()
print(f"Average Grade: {average:.2f}")  # Output: Average Grade: 85.00

# Change school name (affects all students)
Student.change_school_name("Central High")

# Verify school name change
print(student1.get_student_info())  # Output: Alice is a student at Central High.





