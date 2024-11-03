'''
  Define a base class called `Vehicle` with attributes `make` and `model`. Create a subclass called `Car` that inherits from `Vehicle` and adds an attribute `num_doors`. Implement a method in `Car` that returns a string describing the car.
'''
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def car(self):
        return f"This is a {self.make} {self.model} with {self.num_doors}"

# Example usage
my_car = Car("Toyota", "Corolla", 4)
print(my_car.car())
