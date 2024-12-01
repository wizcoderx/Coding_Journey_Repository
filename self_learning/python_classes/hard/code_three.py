'''
   Design a `BookCollection` class that can store multiple `Book` instances. Implement methods `add_book`, `remove_book`, and `find_book` to manage the collection. Also, add a method `most_recent` that returns the most recently published book in the collection. Ensure `find_book` can find books by title, author, or genre.
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

    class BookCollection:
        def __init__(self):
            self.books = []

        def add_book(self):
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            year_published = int(input("Enter the year the book was published: "))
            genre = input("Enter the genre of the book: ")
            self.books.append(Book(title, author, year_published, genre))

        def remove_book(self):
            title = input("Enter the title of the book you want to remove: ")
            for book in self.books:
                if book.title == title:
                    self.books.remove(book)
                    print(f"The book '{title}' has been removed from the collection.")
                else:
                    print(f"The book '{title}' is not in the collection.")

        def find_book(self):
            search_term = input("Select How would you like to search for a book, Enter the number 1) Title 2) Author 3) Genre ")
            if search_term == "1":
                title = input("Enter the title of the book you are looking for: ")
                for title in self.books:
                    if title.title == title:
                        return title
                    else:
                        print(f"The book '{title}' is not in the collection.")
            elif search_term == "2":
                author = input("Enter the author of the book you are looking for: ")
                for book in self.books:
                    if book.author == author:
                        return book
                    else:
                        print(f"The book '{author}' is not in the collection.")

            elif search_term == "3":
                genre = input("Enter the genre of the book you are looking for: ")
                for book in self.books:
                    if book.genre == genre:
                        return book
                    else:
                        print(f"The book '{genre}' is not in the collection.")
            else:
                print("Invalid search term")

        def most_recent(self):
            if len(self.books) == 0:
                print("No books in the collection")
            else:
                self.books.sort(key=lambda x: x.year_published, reverse=True)
                return self.books[0]
            


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
