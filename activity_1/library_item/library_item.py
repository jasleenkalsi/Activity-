""""
Description: A class to manage LibraryItem objects.
Author: Jasleen kalsi
Date: 03 Sept 2024

"""


from genre.genre import Genre

class LibraryItem:

    def __init__(self, item_id: int,title:str, author:str, genre:Genre,is_borrowed: bool):
        # Validate title
        if not title:
            raise ValueError("Title cannot be blank.")
        self._title = title

        # Validate author
        if not author:
            raise ValueError("Author cannot be blank.")
        self._author = author

        # Validate genre
        if genre not in Genre:
            raise ValueError("Invalid Genre.")
        self._genre = genre

        if not isinstance(item_id, int):
            raise ValueError("Item Id must be numeric.")
        self._item_id = item_id

        # Validate title
        if not title:
            raise ValueError("Title cannot be blank.")
        self._title = title

        # Validate author
        if not author:
            raise ValueError("Author cannot be blank.")
        self._author = author

        # Validate genre
        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")
        self._genre = genre

        # Validate is_borrowed
        if not isinstance(is_borrowed, bool):
            raise ValueError("Is Borrowed must be a boolean value.")
        self._is_borrowed = is_borrowed

    # Accessor for item_id
    @property
    def item_id(self):
        return self._item_id

    # Accessor for title
    @property
    def title(self):
        return self._title

    # Accessor for author
    @property
    def author(self):
        return self._author

    # Accessor for genre
    @property
    def genre(self):
        return self._genre

    # Accessor for is_borrowed
    @property
    def is_borrowed(self):
        return self._is_borrowed

   





