'''
   Add attributes `health` (an integer) and `is_trained` (a boolean) to the `Dog` class. Implement a `train` method that improves the dogs `is_trained` attribute to `True` if the dogs `health` is above a certain level(50). Add a `visit_vet` method that adjusts the health level based on random checks and returns the new health level.
'''

class Dog:
    def __init__(self, name, age, breed, health, is_trained=False):
        self.name = name
        self.age = age
        self.breed = breed
        self.health = health
        self.is_trained = is_trained

    def bark(self):
        return f"Woof! My name is {self.name} and I am {self.age} years old."

    def play(self, activity):
        return f"{self.name} is playing {activity}!"

    def age_in_dog_years(self):
        return self.age * 7

    def train(self):
        if self.health > 50:
            self.is_trained = True
            return f"{self.name} is now trained."
        else:
            return f"{self.name} is not healthy enough to be trained."

    def visit_vet(self):
        import random
        health_check = random.randint(1, 100)
        if health_check < 50:
            self.health -= 10
        elif health_check > 50:
            self.health +=10

        return self.health

# Example usage:
dog = Dog(name="Buddy", age=3, breed="Labrador", health=60)
print(dog.train())
print(dog.visit_vet())