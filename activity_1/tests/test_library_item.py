"""
Description: Unit tests for the Book class.
Author: Jasleen kalsi
Date: 03 Sept 2024
Usage: To execute all tests in the terminal execute 
"""
import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

class TestLibraryItem(unittest.TestCase):
    
    def setUp(self):
        """Setup a valid LibraryItem object for reuse in various tests."""
        self.item = LibraryItem(1, "Harry Potter", "John", Genre.FICTION, False)

    def test_init_valid(self):
        """Tests valid initialization of LibraryItem."""
        # Arrange
        item_id = 1
        title = "Harry Potter"
        author = "John"
        genre = Genre.FICTION
        is_borrowed = False
        
        # Act
        item = LibraryItem(item_id, title, author, genre, is_borrowed)
        
        # Assert
        self.assertEqual(item.item_id, item_id)
        self.assertEqual(item.title, title)
        self.assertEqual(item.author, author)
        self.assertEqual(item.genre, genre)
        self.assertEqual(item.is_borrowed, is_borrowed)

    def test_init_blank_title(self):
        """Tests initialization with a blank title."""
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "", "John", Genre.FICTION, False)
        self.assertEqual(str(context.exception), "Title cannot be blank.")

    def test_init_blank_author(self):
        """Tests initialization with a blank author."""
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "Harry Potter", "", Genre.FICTION, False)
        self.assertEqual(str(context.exception), "Author cannot be blank.")

    def test_init_invalid_genre(self):
        """Tests initialization with an invalid genre."""
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "Harry Potter", "John", "InvalidGenre", False)
        self.assertEqual(str(context.exception), "Invalid Genre.")

    def test_init_invalid_item_id(self):
        """Tests initialization with an invalid item_id."""
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem("one", "Harry Potter", "John", Genre.FICTION, True)
        self.assertEqual(str(context.exception), "Item Id must be numeric.")

    def test_init_invalid_is_borrowed(self):
        """Tests initialization with an invalid is_borrowed value."""
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "Harry Potter", "John", Genre.FICTION, "Yes")
        self.assertEqual(str(context.exception), "Is Borrowed must be a boolean value.")

    def test_accessors(self):
        """Tests the accessors of LibraryItem."""
