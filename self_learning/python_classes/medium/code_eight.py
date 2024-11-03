'''
   Create a class `Library` with an attribute `catalog` that holds a dictionary of book titles and the number of available copies for each. Implement methods to `add_book(title, copies)`, `borrow_book(title)`, and `return_book(title)`. Track borrowed books and display which titles are unavailable.
'''
class Library:
    def __init__(self):
        self.catalog = {}
        self.borrowed_books = {}

    #Method to add book
    def add_book(self, title, copies):
        if title in self.catalog:
            self.catalog[title] += copies
        else:
            self.catalog[title] = copies

    #Method to bowered books
    def borrow_book(self, title):
        if title in self.catalog and self.catalog[title] > 0:
            self.catalog[title] -= 1
            self.borrowed_books[title] = self.borrowed_books.get(title, 0) + 1
            return f"You have borrowed {title}"
        else:
            return f"{title} is not available"

    #Method to return a book
    def return_book(self, title):
        if title in self.borrowed_books:
            self.borrowed_books[title] -= 1
            if self.borrowed_books[title] == 0:
                del self.borrowed_books[title]
                self.catalog[title] += 1
                return f"You have returned {title}"
            else:
                return f"You still have {title}"
        else:
            return f"You have not borrowed {title}"

    #Method to display the unaviavlable books
    def list_unavailable_books(self):
        unavailable = [title for title, copies in self.catalog.items() if copies == 0]
        return unavailable if unavailable else "All books are available"
# Create an instance of the Library
library = Library()

# Dummy data for adding books
books_to_add = [
    ("The Great Gatsby", 3),
    ("To Kill a Mockingbird", 2),
    ("1984", 5),
    ("The Catcher in the Rye", 1),
    ("Moby-Dick", 4)
]

# Add books to the library
for title, copies in books_to_add:
    library.add_book(title, copies)

# Check the initial catalog
print("Initial Catalog:", library.catalog)

# Borrow some books
print(library.borrow_book("The Great Gatsby"))  # Should succeed
print(library.borrow_book("1984"))              # Should succeed
print(library.borrow_book("The Catcher in the Rye"))  # Should succeed
print(library.borrow_book("The Catcher in the Rye"))  # Should fail, as only 1 copy was added

# Check the catalog and borrowed books after borrowing
print("Catalog after borrowing:", library.catalog)
print("Borrowed Books:", library.borrowed_books)

# Return some books
print(library.return_book("The Great Gatsby"))  # Should succeed
print(library.return_book("The Catcher in the Rye"))  # Should succeed
print(library.return_book("To Kill a Mockingbird"))  # Should fail, not borrowed

# Check the catalog and borrowed books after returning
print("Catalog after returning:", library.catalog)
print("Borrowed Books after returning:", library.borrowed_books)

# List unavailable books
print("Unavailable Books:", library.list_unavailable_books())



