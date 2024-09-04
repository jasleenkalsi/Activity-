"""
Description: Unit tests for the Book class.
Author: Jasleen kalsi
Date: 03 Sept 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py
"""

import unittest
from library_item import LibraryItem
from genre import Genre

class TestLibraryItem(unittest.TestCase):
     def test_init_valid_parameters(self):
        item = LibraryItem(title="1984", author="George Orwell", isbn="9780451524935")
        self.assertEqual(item.title, "1984")
        self.assertEqual(item.author, "George Orwell")
        self.assertEqual(item.isbn, "9780451524935")
    
     def test_init_blank_title_raises_exception(self):
        with self.assertRaises(ValueError):
            item = LibraryItem(title="", author="George Orwell", isbn="9780451524935")