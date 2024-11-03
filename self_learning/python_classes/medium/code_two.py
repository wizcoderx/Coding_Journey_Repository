'''
   Add a method to the `Circle` class called `perimeter` that calculates and returns the perimeter of the circle using the formula: \( \text{perimeter} = 2 \times \pi \times \text{radius} \). Also, add a method `diameter` that returns the diameter of the circle.
'''
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):

        return math.pi * (self.radius ** 2)

    def perimeter(self):
        permiter_result = 2 * self.radius * math.pi
        return permiter_result

    def diameter(self):
        return 2 * self.radius

if __name__ == "__main__":
    # Create a Circle instance with radius 5
    radius_input = float(input("Enter the radius of the circle: "))
    circle = Circle(radius_input)

    # Print results from each method
    print(f"Radius: {circle.radius}")
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}")
    print(f"Diameter: {circle.diameter():.2f}")