'''
	Update the `Student` class so that each subject in the `grades` dictionary can store multiple grades as a list. Implement a `get_best_subject` method that returns the subject with the highest average grade. Also, add a `print_report_card` method that displays each subject’s average grade in a structured report format.
'''
class Student:

    school_name = "ABC High School"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable
        self.grades = {}  # dictionary to store grades, initially empty

    def get_student_info(self):
        return f"{self.name} is a student at {Student.school_name}."

    @classmethod
    def change_school_name(cls, new_school_name):
        cls.school_name = new_school_name

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def average_grade(self):
        if not self.grades:
            return "No grades available."
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_subjects = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_subjects

    def get_best_subject(self):
        if not self.grades:
            return "No grades available."
        best_subject = max(self.grades, key=lambda subject: sum(self.grades[subject]) / len(self.grades[subject]))
        return best_subject

    def print_report_card(self):
        if not self.grades:
            return "No grades available."
        print(f"Report Card for {self.name}:")
        for subject, grades in self.grades.items():
            average = sum(grades) / len(grades)
            print(f"{subject}: {average:.2f}")
        print(f"Best Subject: {self.get_best_subject()}")
        print(f"Overall Average Grade: {self.average_grade():.2f}")
        print(f"School Name: {Student.school_name}")

# Create a student
student1 = Student("Alice")

# Add some grades
student1.add_grade("Math", 85)
student1.add_grade("Math", 90)
student1.add_grade("English", 92)
student1.add_grade("Science", 78)

# Print the report card
student1.print_report_card()

# Change school name (affects all students)
Student.change_school_name("Central High")

# Verify school name change
print(student1.get_student_info())  # Output: Alice is a student at Central High.
