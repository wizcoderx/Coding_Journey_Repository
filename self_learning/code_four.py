'''
Question 4: Rectangle Area and Perimeter
Create a Rectangle class with:

An __init__ method that takes width and height as parameters.
An area method that returns the area of the rectangle.
A perimeter method that returns the perimeter of the rectangle.
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #Find the area rectraingle
    def area(self):
        return self.width * self.height

    #Find the perimeter
    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 10)
print(rectangle.area())       # Output: 50
print(rectangle.perimeter())  # Output: 30
