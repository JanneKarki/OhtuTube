from entities.book_reference import BookReference
from repositories.references_repository import (
    references_repository as default_references_repository
)
class ReferenceService:
    """ Application logic """
    def __init__(
        self,
        references_repository=default_references_repository
        ):
        self._book = None
        self._references_repository = references_repository

# 
    def collect_inputs(self):
        """Collects entry inputs from the user"""
        print("--------------------------------------------------------------------------------------------------------------------- ")
        print("| If there are several authors or address, separate them with a comma like this: Example1, Example2, Example3        |")
        print("--------------------------------------------------------------------------------------------------------------------- ")

        author = input("> Author: ")
        title = input("> Title: ")
        year = input("> Year: ")
        publisher = input("> Publisher: ")
        address = input("> Address: ")
        reference_id = input("> Create a unique reference id: ")

        self._book = self.set_book(reference_id, author, title, year, publisher, address)


    def set_book(self, reference_id, author, title, year, publisher, address):
        return BookReference(reference_id, author, title, year, publisher, address)


    def confirm_entry(self):
        """Prints the entry attributes for user see and confirm before sending to the database"""
        while True:
            print("")
            print("Reference ID: | Author:            | Title:                       | Year:  | Publisher:         | Address:           |")
            print("---------------------------------------------------------------------------------------------------------------------") 
            print(self._book)
            print("")
            answer = input("Do you want to save this item to database? (y/n): ")
            if answer == "y":
                return self.save_reference_to_db(self._book)
            if answer == "n":
                return
            else:
                print("Answer y(yes) or n(no)")   


    def save_reference_to_db(self, book):
        """Sends the reference object to the database"""
        return self._references_repository.add_book_reference(book)


reference_service = ReferenceService()
