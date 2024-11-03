'''
Add a `genre` attribute to the `Book` class. Implement a method called `is_classic` that returns `True` if the book was published before 1980 and `False` otherwise. Add another method `compare` that takes another book as a parameter and returns the title of the book published earlier
'''
class Book:
    def __init__(self, title, author, year_published, genre):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.genre = genre

    def description(self):
        return f"Title: {self.title}, Author: {self.author}, Year Published: {self.year_published}, Genre: {self.genre}"

    def is_classic(self):
        return self.year_published < 1980

    def compare(self, other_book):
        if self.year_published < other_book.year_published:
            return self.title
        elif self.year_published > other_book.year_published:
            return other_book.title
        else:
            return "Both books were published in the same year."

# Predefined book instances
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
book3 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy")

# Print the descriptions and check if they are classics
print("Book 1 Description:")
print(book1.description())
print(f"Is classic: {book1.is_classic()}")

print("\nBook 2 Description:")
print(book2.description())
print(f"Is classic: {book2.is_classic()}")

print("\nBook 3 Description:")
print(book3.description())
print(f"Is classic: {book3.is_classic()}")

# Compare book1 and book2
earlier_book_1_2 = book1.compare(book2)
print(f"\nThe book published earlier between Book 1 and Book 2 is: {earlier_book_1_2}")

# Compare book1 and book3
earlier_book_1_3 = book1.compare(book3)
print(f"The book published earlier between Book 1 and Book 3 is: {earlier_book_1_3}")

# Compare book2 and book3
earlier_book_2_3 = book2.compare(book3)
print(f"The book published earlier between Book 2 and Book 3 is: {earlier_book_2_3}")
