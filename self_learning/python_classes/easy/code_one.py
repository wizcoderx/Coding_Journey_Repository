'''
 Create a class called `Dog` that has two attributes: `name` and `age`. Implement a method called `bark` that returns a string saying "Woof! My name is {name} and I am {age} years old."
'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"Woof! My name is {self.name} and I am {self.age} years old."


my_dog = Dog("Buddy", 3)

# Call the bark method
print(my_dog.bark())