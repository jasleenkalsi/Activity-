""""
Description: A class to manage LibraryItem objects.
Author: Jasleen kalsi
Date: 03 Sept 2024

"""
from genre import Genre

class LibraryItem:
    def __init__(self, title: str, author: str, genre: Genre):
        """
        Initializes a new LibraryItem instance with title, author, and genre.

        Args:
            title (str): The title of the library item. Cannot be blank.
            author (str): The author of the library item. Cannot be blank.
            genre (Genre): The genre of the library item. Must be a valid Genre.

        Raises:
            ValueError: If the title is blank.
            ValueError: If the author is blank.
            ValueError: If the genre is not a valid Genre.
        """
        # Validate and set title
        if not title():  
            raise ValueError("Title cannot be blank.")
        self._title = title 

        # Validate and set author
        if not author():  
            raise ValueError("Author cannot be blank.")
        self._author = author  

        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")
        self._genre = genre

    @property
    def title (self):
        return self._title
        

    @property
    def author(self):
        """Returns the author of the library item."""
        return self._author

    @property
    def genre(self):
        """Returns the genre of the library item."""
        return self._genre




