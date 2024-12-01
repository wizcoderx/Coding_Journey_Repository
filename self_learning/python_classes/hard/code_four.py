'''
   Add a `fuel_log` attribute to the `Car` class, which stores a list of fuel refills (in gallons) over time. Implement a method `add_fuel(amount)` to add fuel to this log, and a method `average_fuel_usage` that calculates the average fuel used per refill. Add a `service_due` method that returns `True` if the car has traveled more than a certain threshold (e.g., 10,000 miles) since the last service.
'''

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, num_doors, mileage, fuel_capacity, fuel_log=None):
        super().__init__(make, model)
        self.num_doors = num_doors
        self.mileage = mileage
        self.fuel_capacity = fuel_capacity
        self.fuel_log = fuel_log if fuel_log is not None else []

    def car(self):
        return f"This is a {self.make} {self.model} with {self.num_doors} doors."

    def range(self):
        return self.mileage * self.fuel_capacity

    def is_fuel_efficient(self):
        return self.mileage > 20

    def add_fuel(self, amount):
        self.fuel_log.append(amount)

    def average_fuel_usage(self):
        if len(self.fuel_log) > 0:
            return sum(self.fuel_log) / len(self.fuel_log)
        else:
            return 0

    def service_due(self, last_service_mileage):
        if self.mileage - last_service_mileage > 10000:
            return True
        else:
            return False


# Example usage
my_car = Car("Toyota", "Corolla", 4, 31000, 13)  # Added mileage and fuel capacity
my_car.add_fuel(10)
my_car.add_fuel(15)

print(my_car.car())
print(f"Range: {my_car.range()} miles")
print(f"Is fuel efficient? {'Yes' if my_car.is_fuel_efficient() else 'No'}")
print(f"Average fuel usage: {my_car.average_fuel_usage()} gallons per refill")

# Check if service is due
last_service_mileage = 5000
print(f"Service due: {my_car.service_due(last_service_mileage)}")
