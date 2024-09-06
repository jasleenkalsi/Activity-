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
