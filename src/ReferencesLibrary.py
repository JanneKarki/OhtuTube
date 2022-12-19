from repositories.references_repository import ReferencesRepository
from services.reference_service import ReferenceService
from stub_io import StubIO
from ui.ui import Ui
from initialize_database import initialize_database

COLUMNS = {"id" : 0,
            "author" : 1,
            "title" : 2,
            "year" : 3,
            "publisher" : 4,
            "address"   : 5

}

class ReferencesLibrary:
    def __init__(self):
        self.test_database = "test_database.sqlite"
        self.refrences_repository = ReferencesRepository(self.test_database)
        self._references_service = ReferenceService(self.refrences_repository)
        self._io = StubIO()

        self._ui = Ui(self._io, self._references_service)
        self._ui.set_test()

        initialize_database(self.test_database)

    def start_app(self):
        self._ui.start()

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}")

    def add_book_reference(self, reference_id, author, title, year, publisher, address, selected):
        book = self._references_service.set_book(reference_id, author, title, year, publisher, address, selected)
        self._references_service.save_reference_to_db(book)


    def search_output_should_contain_value_with_parameter(self, value, parameter, column):
        column = COLUMNS[column]
        results = self._ui.display_search_book(parameter)
        if results:
            for result in results:
                if not value in result[column]:
                    raise AssertionError(
                        f"Output \"{value}\" is not in {str(result)}")


    def search_output_should_not_contain_unmatching_results(self, value, parameter, column):
        column = COLUMNS[column]
        results = self._ui.display_search_book(parameter)
        if results:
            for result in results:
                if value not in result[column]:
                    raise AssertionError(
                    f"Search with \"{value}\" included unmatching results ")


    def database_should_be_empty(self):
        results = self._ui.display_search_book_by_desc_datetime()
        if results:
            raise AssertionError("Database is not empty!")


    def reference_not_in_database(self, parameter, column):
        column = COLUMNS[column]
        result = self._ui.display_search_book(parameter)
        print(result)
        if result:
            raise AssertionError("Reference is still in the database!")
