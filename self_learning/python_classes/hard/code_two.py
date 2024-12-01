'''
   Add a `compare` method to the `Circle` class that takes another circle as input and returns which circle is larger in terms of area. Also, implement a static method `circle_from_diameter(diameter)` that takes a diameter as input and returns a `Circle` instance with that diameter.
'''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter of the circle."""
        return 2 * self.radius * math.pi

    @property
    def diameter(self):
        """Calculate and return the diameter of the circle."""
        return 2 * self.radius

    def compare(self, other_circle):
        """
        Compare the area of this circle with another circle.
        Args:
            other_circle (Circle): The circle to compare with.
        Returns:
            str: A message indicating which circle is larger.
        """
        if self.area() > other_circle.area():
            return "This circle is larger"
        elif self.area() < other_circle.area():
            return "The other circle is larger"
        else:
            return "Both circles are of the same size"

    @staticmethod
    def circle_from_diameter(diameter):
        """
        Create a Circle instance given its diameter.
        Args:
            diameter (float): The diameter of the circle.
        Returns:
            Circle: A Circle instance with the calculated radius.
        """
        radius = diameter / 2
        return Circle(radius)

# Main program
if __name__ == "__main__":
    # Create a Circle instance with user-provided radius
    radius_input = float(input("Enter the radius of the circle: "))
    circle = Circle(radius_input)

    # Print results from each method
    print(f"Radius: {circle.radius}")
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}")
    print(f"Diameter: {circle.diameter:.2f}")

    # Create another Circle instance using the static method
    diameter_input = float(input("Enter the diameter of another circle: "))
    another_circle = Circle.circle_from_diameter(diameter_input)

    print(f"\nAnother Circle:")
    print(f"Radius: {another_circle.radius}")
    print(f"Area: {another_circle.area():.2f}")
    print(f"Perimeter: {another_circle.perimeter():.2f}")
    print(f"Diameter: {another_circle.diameter:.2f}")

    # Compare the two circles
    comparison_result = circle.compare(another_circle)
    print(f"\nComparison: {comparison_result}")
