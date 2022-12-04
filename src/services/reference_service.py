from entities.book_reference import BookReference
from repositories.references_repository import ReferencesRepository


class ReferenceService:
    """ Application logic """

    def __init__(
        self,
        references_repository=ReferencesRepository
    ):
        self._book = None
        self._references_repository = references_repository

    def search(self, search):
        """Gets book reference by author from the db
           and prints the result
        """

        information = self.references_search(search)
        self.print_book_summary()
        if len(information) > 0:
            for info in information:
                book = self.set_book(info)
                print(book)
                print(117 * "-")
        else:
            print("\n")
            print(f"References with keyword {search} not found")
            print("\n")
        return information

    def search_all_ordered_by_descending_datetime(self):
        """Gets book reference by author from the db
        and prints the result
        """

        information = self._references_repository.get_all_book_references_order_by_desc_datetime()
        self.print_book_summary()
        if len(information) > 0:
            for info in information:
                book = self.set_book(info)
                print(book)
                print(117 * "-")
        else:
            print("\n")
            print("References not found")
            print("\n")
        return information

    @classmethod
    def set_book(cls, book_information):
        reference_id = book_information[0]
        author = book_information[1]
        title = book_information[2]
        year = book_information[3]
        publisher = book_information[4]
        address = book_information[5]
        
        return BookReference(reference_id, author, title, year, publisher, address)

    def save_reference_to_db(self, book):
        """Sends the reference object to the database"""
        return self._references_repository.add_book_reference(book)

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
