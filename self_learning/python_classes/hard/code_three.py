'''
   Design a `BookCollection` class that can store multiple `Book` instances. Implement methods `add_book`, `remove_book`, and `find_book` to manage the collection. Also, add a method `most_recent` that returns the most recently published book in the collection. Ensure `find_book` can find books by title, author, or genre.
'''
import math

class Book:
    def __init__(self, title, author, year_published, genre):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.genre = genre

    def description(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year_published}, Genre: {self.genre}"

    def is_classic(self):
        return self.year_published < 1980

    def compare(self, other_book):
        if self.year_published < other_book.year_published:
            return self.title
        elif self.year_published > other_book.year_published:
            return other_book.title
        else:
            return "Both books were published in the same year."


class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a Book object to the collection."""
        self.books.append(book)
        print(f"Book '{book.title}' added to the collection.")

    def remove_book(self, title):
        """Remove a book by title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed from the collection.")
                return
        print(f"The book '{title}' is not in the collection.")

    def find_book(self, search_by, value):
        """
        Find a book by title, author, or genre.
        Args:
            search_by (str): 'title', 'author', or 'genre'.
            value (str): The value to search for.
        Returns:
            Book or None: The matching book, if found.
        """
        for book in self.books:
            if getattr(book, search_by, "").lower() == value.lower():
                return book
        print(f"No book found for {search_by}: '{value}'.")
        return None

    def most_recent(self):
        """Return the most recently published book."""
        if not self.books:
            print("No books in the collection.")
            return None
        most_recent_book = max(self.books, key=lambda book: book.year_published)
        return most_recent_book


# Example usage:
if __name__ == "__main__":
    # Predefined books
    book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
    book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
    book3 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy")

    # Create a book collection
    collection = BookCollection()

    # Add books to the collection
    collection.add_book(book1)
    collection.add_book(book2)
    collection.add_book(book3)

    # Find a book by title
    print("\nSearching for a book by title:")
    found_book = collection.find_book("title", "The Great Gatsby")
    if found_book:
        print(found_book.description())

    # Find a book by author
    print("\nSearching for a book by author:")
    found_book = collection.find_book("author", "J.K. Rowling")
    if found_book:
        print(found_book.description())

    # Remove a book
    print("\nRemoving a book:")
    collection.remove_book("The Great Gatsby")

    # Show the most recent book
    print("\nMost recent book in the collection:")
    most_recent = collection.most_recent()
    if most_recent:
        print(most_recent.description())
