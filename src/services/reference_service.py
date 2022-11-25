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

    def collect_inputs(self):
        """Collects entry inputs from the user"""
        self.print_add_reference_title()

        author = input("> Author (Last name, First name): ")
        title = input("> Title: ")
        year = input("> Year: ")
        publisher = input("> Publisher: ")
        address = input("> Address: ")
        reference_id = input("> Create a unique reference id: ")

        self._book = self.set_book(
            reference_id, author, title, year, publisher, address)

    def set_book(self, reference_id, author, title, year, publisher, address):
        return BookReference(reference_id, author, title, year, publisher, address)

    def confirm_entry(self):
        """Prints the entry attributes for user see and confirm
            before sending to the database"""
        while True:
            self.print_book_summary()
            answer = input(
                "Do you want to save this item to database? (y/n): ")
            if answer == "y":
                return self.save_reference_to_db(self._book)
            if answer == "n":
                print("\n")
                break
            print("Answer y(yes) or n(no)")

    def save_reference_to_db(self, book):
        """Sends the reference object to the database"""
        return self._references_repository.add_book_reference(book)

    def print_book_attr_titles(self):
        """Creates a row of titles of the book reference attributes
        which can be used in the UI """

        reference_id = "Reference ID"
        author = "Author"
        title = "Title"
        year = "Year"
        publisher = "Publisher"
        address = "Address"

        print(
            f"{reference_id:13} | {author:19} | {title:28} | " +
            f"{year:6} | {publisher:18} | {address:18}"
        )
        print(117 * "-")

    def print_add_reference_title(self):
        """Title of Add new reference"""

        print(117 * "-")
        print("| ADD NEW REFERENCE")
        print(117 * "-")

    def print_book_summary(self):
        """Table of a single book reference with titles
            for the attributes"""
        print("")
        self.print_book_attr_titles()
        print(self._book)
        print("")


reference_service = ReferenceService()
