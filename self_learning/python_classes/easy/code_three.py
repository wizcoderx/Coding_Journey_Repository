'''
Create a class named `Book` that has attributes for `title`, `author`, and `year_published`. Use the constructor to initialize these attributes. Also, create a method called `description` that returns a string summarizing the book's details.
'''
class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def description(self):
        return f"Title: {self.title}, Author: {self.author}, Year Published: {self.year_published}"

launch = Book('Rich Dad Poor Dad', 'Robert.K', 2011)
print(launch.year_published())

