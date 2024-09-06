""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""

# activity_01_main.py

# Import necessary modules here
from genre.genre import Genre
from library_item.library_item import LibraryItem

def main():
    try:
        item = LibraryItem(1, "Harry Potter", "John", Genre.FICTION, False)
        print(f"Created LibraryItem: ID={item.item_id}, Title='{item.title}', Author='{item.author}', Genre='{item.genre}', Is Borrowed={item.is_borrowed}")
    except ValueError as e:
        print(f"Error creating LibraryItem: {e}")

    try:
        item = LibraryItem("one", "Harry Potter", "John", Genre.FICTION, False)
    except ValueError as e:
        print(f"Error creating LibraryItem with invalid item_id: {e}")

    try:
        item = LibraryItem(1, "Harry Potter", "John", Genre.FICTION, "Yes")
    except ValueError as e:
        print(f"Error creating LibraryItem with invalid is_borrowed: {e}")

if __name__ == "__main__":
    main()


