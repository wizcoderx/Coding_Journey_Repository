'''
 Define a class called `Circle` that has an attribute `radius`. Implement a method called `area` that calculates and returns the area of the circle using the formula: \( \text{area} = \pi \times \text{radius}^2 \).

'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

my_area = Circle(5)
print(my_area.area())