'''
   Add a `breed` attribute to the `Dog` class. Implement a method called `play` that takes an activity (e.g., "fetch") as a parameter and returns a string like "{name} is playing {activity}!". Add a method `age_in_dog_years` that calculates and returns the dog’s age in "dog years" (using a multiplier of 7).
'''

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return f"Woof! My name is {self.name} and I am {self.age} years old."

    def play(self, activity):
        return f"{self.name} is playing {activity}!"

    def age_in_dog_years(self):
        return self.age * 7

# Creating instances of the Dog class
dog1 = Dog(name="Buddy", age=4, breed="Golden Retriever")
dog2 = Dog(name="Max", age=7, breed="German Shepherd")

# Testing the bark method
print(dog1.bark())  # Expected: "Woof! My name is Buddy and I am 4 years old."
print(dog2.bark())  # Expected: "Woof! My name is Max and I am 7 years old."

# Testing the play method with different activities
print(dog1.play("fetch"))  # Expected: "Buddy is playing fetch!"
print(dog2.play("tug-of-war"))  # Expected: "Max is playing tug-of-war!"

# Testing the age_in_dog_years method
print(f"{dog1.name} is {dog1.age_in_dog_years()} dog years old.")  # Expected: "Buddy is 28 dog years old."
print(f"{dog2.name} is {dog2.age_in_dog_years()} dog years old.")  # Expected: "Max is 49 dog years old."
