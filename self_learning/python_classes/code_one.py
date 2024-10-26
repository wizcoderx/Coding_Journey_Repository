"""
Question 1: Basic Book Details
Create a class called Book with the following:

An __init__ method that takes title, author, and year as parameters and initializes them as instance variables.
A method get_info that returns a string in the format: "<title> by <author>, published in <year>."

"""


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    #The below is the method get_info
    def get_info(self):
        return f"{self.title} by {self.author}, published in {self.year}"

book = Book("1984", "George Orwell", 1949)
print(book.get_info())  # Output: "1984 by George Orwell, published in 1949"
