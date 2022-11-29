from entities.book_reference import BookReference
from repositories.references_repository import (
    references_repository as default_references_repository
)

from simple_term_menu import TerminalMenu

class ReferenceService:
    """ Application logic """

    def __init__(
        self,
        references_repository=default_references_repository
    ):
        self._book_references = {}
        self._references_repository = references_repository
        self._chosen_references = []

    def search(self, search):
        """Gets book reference by author from the db
           and prints the result
        """
        
        self._book_references = {}
        information = self.references_search(search)
        self.create_book_references(information)
        self.print_book_summary()
        for book_ref in self._book_references:
            print(self._book_references[book_ref])
            print(117 * "-")
        else:
            print("\n")
            print(f"References with keyword {search} not found")
            print("\n")
        self.select_references()

    def create_book_references(self, database_book_references):
        information = database_book_references
        if len(information) > 0:
            for info in information:
                reference_id = info[0]
                author = info[1]
                title = info[2]
                year = info[3]
                publisher = info[4]
                address = info[5]
                book = self.set_book(reference_id, author,
                                     title, year, publisher, address)
                self._book_references[book.reference_id] = book

    def select_references(self):
        print("Please select references to convert into bibtex form. Press 'ctrl-c' to go back without selecting")
        print("Select reference id:")
        print(" ")
        terminal_menu = self.terminal_menu(self._book_references)
        terminal_menu.show()
        if terminal_menu.chosen_menu_entries:
            for reference_id in terminal_menu.chosen_menu_entries:
                self._chosen_references.append(reference_id)
    
    def terminal_menu(self, entries):
        terminal_menu = TerminalMenu(
        entries,
        multi_select=True,
        show_multi_select_hint=True,
         accept_keys=("e"),
        menu_cursor = ">",
        menu_cursor_style=("fg_red", "bold"),
        menu_highlight_style=("bg_red", "fg_yellow")
        )
        return terminal_menu

    def unselect_references(self):
        print("Press 'ctrl-c' to go back without unselecting")
        print("Unselect reference id:")
        terminal_menu = self.terminal_menu(self._chosen_references)
        terminal_menu.show()
        if terminal_menu.chosen_menu_entries:
            for reference_id in terminal_menu.chosen_menu_entries:
                if reference_id:
                    self._chosen_references.remove(reference_id) 

    def search_all_ordered_by_descending_datetime(self):
        """Gets book reference by author from the db
        and prints the result
        """
        self.print_book_summary()
        self.fetch_all_book_references()
        if len(self._book_references) > 0:
                for reference_id in self._book_references:
                    print(self._book_references[reference_id])
                    print(117 * "-")
        else:
            print("\n")
            print("References not found")
            print("\n")
        self.select_references()

    def fetch_all_book_references(self):
        information = self._references_repository.get_all_book_references_order_by_desc_datetime()
        self._book_references = {}
        if len(information) > 0:
            for info in information:
                reference_id = info[0]
                author = info[1]
                title = info[2]
                year = info[3]
                publisher = info[4]
                address = info[5]
                selected = info[6]
                book = self.set_book(reference_id, author,
                                     title, year, publisher, address, selected)
                self._book_references[reference_id] = book

    @classmethod
    def set_book(cls, reference_id, author, title, year, publisher, address, selected=False):
        return BookReference(reference_id, author, title, year, publisher, address, selected)

    def save_reference_to_db(self, book):
        """Sends the reference object to the database"""
        self._references_repository.add_book_reference(book)
        self._book_references.append(book)

    @classmethod
    def print_book_attr_titles(cls):
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

    @classmethod
    def print_add_reference_title(cls):
        """Title of Add new reference"""

        print(117 * "-")
        print("| ADD NEW REFERENCE")
        print(117 * "-")

    def print_book_summary(self):
        """Table of a single book reference with titles
            for the attributes"""
        print(" ")
        self.print_book_attr_titles()

    def get_all_book_references_order_by_desc_datetime(self):
        result = self._references_repository.get_all_book_references_order_by_desc_datetime()
        return result

    def references_search(self, search):
        return self._references_repository.get_book_references_by_search(search)


reference_service = ReferenceService()
