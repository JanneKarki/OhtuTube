import os
from entities.book_reference import BookReference
from repositories.references_repository import ReferencesRepository


class ReferenceService:
    """ Application logic """

    def __init__(
        self,
        references_repository=ReferencesRepository
    ):
        self._references_repository = references_repository
        self._book_references = {}
        self.maximum_row = 5
        self.information = None

    def reset(self):
        self._book_references = {}
        self.maximum_row = 5

    def search(self, search):
        """Gets book references by keyword from the db
           and shows the results
        """
        information = self.references_search(search)
        if information:
            self.create_book_references(information)
            return information
        print("\n")
        print(f"References with keyword {search} not found")
        print("\n")
        return None

    def search_all_ordered_by_descending_datetime(self):
        """Gets all book references from the db and shows the results"""
        self._book_references = {}
        information = self.get_all_book_references_order_by_desc_datetime()
        if information:
            self.create_book_references(information)
            return information
        print("There isn't any book references added.")
        return None

    def get_book_references_and_max_row(self):
        return (self._book_references, self.maximum_row)

    def create_book_references(self, information):
        self.reset()
        if information:
            for info in information:
                book = self.create_book(info)
                self._book_references[self.maximum_row] = book
                self.maximum_row += 2

    def show_selected_references(self):
        information = self._references_repository.get_selected_book_references()
        if information:
            self.create_book_references(information)
            return information
        print("There isn't any book references selected.")
        return None

    def create_bib_file(self):
        self.reset()
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(
            basepath, "..", "generated_file.bib"))
        with open(filepath, "w", encoding="utf-8") as myfile:
            information = self._references_repository.get_selected_book_references()
            self.create_book_references(information)
            for book in self._book_references.items():
                bibtex_form = book[1].bibtex
                myfile.write(bibtex_form)
                myfile.write("\n")

    def create_book(self, info):
        reference_id = info[0]
        author = info[1]
        title = info[2]
        year = info[3]
        publisher = info[4]
        address = info[5]
        selected = info[6]
        return self.set_book(reference_id, author,
                             title, year, publisher, address, selected)

    def fetch_all_book_references(self):
        self.reset()
        information = self._references_repository.get_all_book_references_order_by_desc_datetime()
        book_number = 5
        if len(information) > 0:
            for info in information:
                book = self.create_book(info)
                self._book_references[book_number] = book
                book_number += 2

    @classmethod
    def set_book(cls, reference_id, author, title, year, publisher, address, selected=False):
        return BookReference(reference_id, author, title, year, publisher, address, selected)

    def save_reference_to_db(self, book):
        """Sends the reference object to the database"""
        self._references_repository.add_book_reference(book)

    def update_selected_reference(self, book):
        reference_id = book.reference_id
        option = book.selected
        self._references_repository.update_selected(
            option, reference_id=reference_id)

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
        return (
            f"  Select | {reference_id:13} | {author:19} | {title:28} | " +
            f"{year:6} | {publisher:18} | {address:18}"
        )

    @classmethod
    def print_add_reference_title(cls):
        """Title of Add new reference"""
        print(117 * "-")
        print("| ADD NEW REFERENCE")
        print(117 * "-")

    def get_all_book_references_order_by_desc_datetime(self):
        result = self._references_repository.get_all_book_references_order_by_desc_datetime()
        return result

    def references_search(self, search):
        return self._references_repository.get_book_references_by_search(search)


reference_service = ReferenceService()
