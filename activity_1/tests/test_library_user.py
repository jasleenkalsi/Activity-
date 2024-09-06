"""
Description: Unit tests for the LibraryUser class.
Author: jasleen 
Date: 03 sept 2024
Usage: To execute all tests in the terminal execute 
the following command:
    
"""

# test_library_user.py

import unittest
from borrower_status.borrower_status import BorrowerStatus
from library_user.library_user import LibraryUser

import unittest
from borrower_status.borrower_status import BorrowerStatus
from library_user.library_user import LibraryUser

class TestLibraryUser(unittest.TestCase):
    
    def setUp(self):
        """Setup a valid user object for reuse in various tests."""
        self.user = LibraryUser(100, "Jasleen", "jasleen@gmail.com", BorrowerStatus.ACTIVE)

    def test_init_valid(self):
        """Tests valid initialization of LibraryUser."""
        # Arrange
        user_id = 100
        name = "Jasleen"
        email = "jasleen@gmail.com"
        status = BorrowerStatus.ACTIVE
        
        # Act
        user = LibraryUser(user_id, name, email, status)
        
        # Assert
        self.assertEqual(user.user_id, user_id)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
        self.assertEqual(user.borrower_status, status)

    def test_init_invalid_user_id(self):
        """Tests initialization with invalid user_id."""
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryUser("abc", "Jasleen", "jasleen@gmail.com", BorrowerStatus.ACTIVE)
        self.assertEqual(str(context.exception), "User Id must be numeric.")

        with self.assertRaises(ValueError) as context:
            LibraryUser(50, "Jasleen", "jasleen@gmail.com", BorrowerStatus.ACTIVE)
        self.assertEqual(str(context.exception), "Invalid User Id.")

    def test_init_blank_name(self):
        """Tests initialization with blank name."""
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryUser(100, "", "jasleen@gmail.com", BorrowerStatus.ACTIVE)
        self.assertEqual(str(context.exception), "Name cannot be blank.")

    def test_init_invalid_email(self):
        """Tests initialization with invalid email."""
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryUser(100, "Jasleen", "invalid-email", BorrowerStatus.ACTIVE)
        self.assertEqual(str(context.exception), "Invalid email address.")

    def test_init_invalid_borrower_status(self):
        """Tests initialization with invalid borrower status."""
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryUser(100, "Jasleen", "jasleen@gmail.com", "InvalidStatus")
        self.assertEqual(str(context.exception), "Invalid Borrower Status.")

    def test_borrow_item_delinquent_user(self):
        """Tests borrow_item method for a DELINQUENT user."""
        # Arrange
        delinquent_user = LibraryUser(101, "Bob", "bob@gmail.com", BorrowerStatus.DELINQUENT)
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            delinquent_user.borrow_item()
        self.assertEqual(str(context.exception), "Bob cannot borrow an item due to their DELINQUENT status.")

    def test_borrow_item_active_user(self):
        """Tests borrow_item method for an ACTIVE user."""
        # Act
        result = self.user.borrow_item()
        
        # Assert
        self.assertEqual(result, "Jasleen is eligible to borrow the item.")

    def test_return_item_delinquent_user(self):
        """Tests return_item method for a DELINQUENT user."""
        # Arrange
        delinquent_user = LibraryUser(101, "Bob", "bob@gmail.com", BorrowerStatus.DELINQUENT)
        
        # Act
        result = delinquent_user.return_item()
        
        # Assert
        self.assertEqual(result, "Item successfully returned. Bob has returned the item, status now changed to: ACTIVE.")
        self.assertEqual(delinquent_user.borrower_status, BorrowerStatus.ACTIVE)

    def test_return_item_active_user(self):
        """Tests return_item method for an ACTIVE user."""
        # Act
        result = self.user.return_item()
        
        # Assert
        self.assertEqual(result, "Item successfully returned.")

if __name__ == "__main__":
    unittest.main()
