'''
   In the `Car` class, add attributes for `mileage` and `fuel_capacity`. Implement a method `range` that calculates and returns the maximum distance the car can travel on a full tank. Also, add a method `is_fuel_efficient` that returns `True` if the car has a mileage greater than 20 mpg, `False` otherwise.
'''

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, num_doors, milage, fuel_capacity):
        super().__init__(make, model)
        self.num_doors = num_doors
        self.milage = milage
        self.fuel_capacity = fuel_capacity

    def car(self):
        return f"This is a {self.make} {self.model} with {self.num_doors}"

    def range(self):
        return self.milage * self.fuel_capacity

    def is_fuel_efficient(self):
        if self.milage > 20:
            return True
        else:
            return False

# Example usage
my_car = Car("Toyota", "Corolla", 4, 31, 13)  # Added mileage and fuel capacity
print(my_car.car())
print(f"Range: {my_car.range()} miles")
print(f"Is fuel efficient? {'Yes' if my_car.is_fuel_efficient() else 'No'}")
