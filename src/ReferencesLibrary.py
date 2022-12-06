from repositories.references_repository import ReferencesRepository
from services.reference_service import ReferenceService
from stub_io import StubIO
from ui.ui import Ui
from initialize_database import initialize_database


class ReferencesLibrary:
    def __init__(self):
        self.test_database = "test_database.db"
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

    def add_book_reference(self, reference_id, author, title, year, publisher, address):
        book = self._references_service.set_book(reference_id, author, title, year, publisher, address)
        self._references_service.save_reference_to_db(book)


    def search_output_should_contain_value_with_parameter(self, value, parameter):
        result = self._ui.display_search_book(parameter)
        if result:
            if not value in result[0][1]:
                raise AssertionError(
                    f"Output \"{value}\" is not in {str(result)}")