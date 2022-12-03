import curses
from curses import wrapper
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
        self.maximum_row = None
        self.current_book_number = 5
        self.current_row = 5

    def reset(self):
        self._book_references = {}
        self.maximum_row = None
        self.current_book_number = 5
        self.current_row = 5

    def search(self, search):
        """Gets book references by keyword from the db
           and shows the results
        """
        self.reset()
        information = self.references_search(search)
        if information:
            self.create_book_references(information)
            print("")
            wrapper(self.run_terminal)
        else:
            print("\n")
            print(f"References with keyword {search} not found")
            print("\n")

    def search_all_ordered_by_descending_datetime(self):
        """Gets all book references from the db and shows the results"""
        self.reset()
        self._book_references = {}
        information = self.get_all_book_references_order_by_desc_datetime()
        if information:
            self.create_book_references(information)
            wrapper(self.run_terminal)
        else:
            print("There isn't any book references added.")

    def print_terminal_menu(self, win):
        the_line = "-"
        height, width = 5, 10
        text = (
            """Toggle selection by RIGHT ARROW, RETURN: LEFT ARROW, UP and DOWN ARROWS.""")
        win.addstr(
            1, width, text)
        win.addstr(2, width, 117*"-")
        win.addstr(3, width, self.print_book_attr_titles())
        win.addstr(4, width, 117*"-")
        self.current_book_number = max(self.current_book_number, 5)
        for book_number in range(self.current_book_number, self.maximum_row, 2):
            try:
                if self.current_row == height:
                    win.attron(curses.color_pair(1))
                    win.addstr(height, width, str(
                        self._book_references[book_number]))
                    win.attroff(curses.color_pair(1))
                    win.addstr(height+1, width, str(the_line*117))
                else:
                    win.addstr(height, width, str(
                        self._book_references[book_number]))
                    win.addstr(height+1, width, str(the_line*117))
            except curses.error:
                pass
            win.refresh()
            height += 2
        win.refresh()

    def run_terminal(self, win):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

        self.print_terminal_menu(win)
        while self.current_book_number <= self.maximum_row:
            try:
                key = win.getch()
            except KeyError:
                key = None
            if key == curses.KEY_UP:
                self.current_book_number -= 2
            elif key == curses.KEY_DOWN:
                self.current_book_number += 2
            elif key == curses.KEY_LEFT:
                break
            elif key == curses.KEY_RIGHT:
                if self._book_references[self.current_book_number].selected:
                    self._book_references[self.current_book_number].selected = False
                    reference_id = self._book_references[self.current_book_number].reference_id
                    self._references_repository.update_selected(
                        option=False, reference_id=reference_id)
                else:
                    self._book_references[self.current_book_number].selected = True
                    reference_id = self._book_references[self.current_book_number].reference_id
                    self._references_repository.update_selected(
                        option=True, reference_id=reference_id)
            elif key == curses.KEY_ENTER or key in [10, 13]:
                break
            self.print_terminal_menu(curses.newwin(0, 0))
            win.refresh()

    def create_book_references(self, database_book_references):
        information = database_book_references
        self.current_row = 5
        self.maximum_row = 5
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
                self._book_references[self.maximum_row] = book
                self.maximum_row += 2

    def show_selected_references(self):
        self.reset()
        information = self._references_repository.get_selected_book_references()
        if information:
            self.create_book_references(information)
            wrapper(self.run_terminal)
        else:
            print("There isn't any book references selected.")

    def create_bib_file(self):
        self.reset()
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(
            basepath, "..", "generated_file.bib"))
        with open(filepath, "w", encoding="utf-8") as myfile:
            information = self._references_repository.get_selected_book_references()
            self.create_book_references(information)
            for book in self._book_references.items():
                bibtex_form = book.bibtex
                myfile.write(bibtex_form)
                myfile.write("\n")

    def fetch_all_book_references(self):
        information = self._references_repository.get_all_book_references_order_by_desc_datetime()
        book_number = 5
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
                self._book_references[book_number] = book
                book_number += 2

    @classmethod
    def set_book(cls, reference_id, author, title, year, publisher, address, selected=False):
        return BookReference(reference_id, author, title, year, publisher, address, selected)

    def save_reference_to_db(self, book):
        """Sends the reference object to the database"""
        self._references_repository.add_book_reference(book)

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
