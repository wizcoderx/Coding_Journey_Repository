'''
   Create a `Movie` class with attributes `title`, `genre`, `release_year`, and `available_copies`. Implement a `RentalService` class that has a collection of movies and manages movie rentals. Add methods for `rent_movie(title)`, `return_movie(title)`, and `get_available_movies_by_genre(genre)`. Also, add a `recommend_movie` method that suggests a random movie in the same genre as a recently rented one.
'''

class Movie:
    def __init__(self, title, genre, release_year, available_copies):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.available_copies = available_copies

class RentalService:

    def rent_movie(title):
        # Find the movie with the given title and decrement its available copies
        