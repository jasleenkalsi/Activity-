""""
Description: A class to manage User objects.
Author: Jasleen kalsi
Date:  03 sept 2024
"""


from borrower_status.borrower_status import BorrowerStatus

class LibraryUser:
    def __init__(self, user_id: int, name: str, email: str, borrower_status: BorrowerStatus):
        """
        Initializes a LibraryUser instance with the provided values.
        """
        if not isinstance(user_id, int):
            raise ValueError("User Id must be numeric.")
        if user_id <= 99:
            raise ValueError("Invalid User Id.")
        self._user_id = user_id

        if not name:
            raise ValueError("Name cannot be blank.")
        self._name = name

        if not self._is_valid_email(email):
            raise ValueError("Invalid email address.")
        self._email = email

        if not isinstance(borrower_status, BorrowerStatus):
            raise ValueError("Invalid Borrower Status.")
        self._borrower_status = borrower_status

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def borrower_status(self):
        return self._borrower_status

    def _is_valid_email(self, email: str) -> bool:
        """
        Validates if the provided email address is valid.
        A simple validation that checks for the presence of '@' and '.'.
        """
        return "@" in email and "." in email

    def borrow_item(self) -> str:
        if self._borrower_status == BorrowerStatus.DELINQUENT:
            raise Exception(f"{self._name} cannot borrow an item due to their DELINQUENT status.")
        return f"{self._name} is eligible to borrow the item."

    def return_item(self) -> str:
        if self._borrower_status == BorrowerStatus.DELINQUENT:
            self._borrower_status = BorrowerStatus.ACTIVE
            return f"Item successfully returned. {self._name} has returned the item, status now changed to: ACTIVE."
        return "Item successfully returned."

