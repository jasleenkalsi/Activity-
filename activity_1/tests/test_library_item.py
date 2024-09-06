"""
Description: Unit tests for the Book class.
Author: Jasleen kalsi
Date: 03 Sept 2024
Usage: To execute all tests in the terminal execute 
"""
import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

class TestLibraryItem(unittest.TestCase):
    def setUp(self):
        self.item = LibraryItem(1, "Harry Potter", "John", Genre.FICTION, False)
    
    def test_init_valid(self):
        item = LibraryItem(1, "Harry Potter", "John", Genre.FICTION, False)
        self.assertEqual(item.item_id, 1)
        self.assertEqual(item.title, "Harry Potter")
        self.assertEqual(item.author, "John")
        self.assertEqual(item.genre, Genre.FICTION)
        self.assertEqual(item.is_borrowed, False)

    def test_init_blank_title(self):
     #Act None
     #Arrange
     
    #assert
     with self.assertRaises(ValueError):
      library_item = LibraryItem(1,"", "John", Genre.FICTION,False)

    def test_init_blank_author(self):        
       with self.assertRaises(ValueError):            
          LibraryItem(1,"Harry Potter", "", Genre.FICTION,False)    

    def test_init_invalid_genre(self): 
       with self.assertRaises(ValueError): 
        LibraryItem(1,"Harry Potter", "John", "InvalidGenre",False) 

    def test_init_invalid_item_id(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem("one", "Harry Potter", "John", Genre.FICTION, True)
        self.assertEqual(str(context.exception), "Item Id must be numeric.")

    def test_init_invalid_is_borrowed(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "Harry Potter", "John", Genre.FICTION, "Yes")
        self.assertEqual(str(context.exception), "Is Borrowed must be a boolean value.")

    def test_accessors(self):

        self.assertEqual(self.item.title, "Harry Potter")
        self.assertEqual(self.item.author, "John")
        self.assertEqual(self.item.genre, Genre.FICTION)
        self.assertEqual(self.item.item_id, 1)
        self.assertEqual(self.item.is_borrowed, False)

if __name__ == "__main__":
    unittest.main()
