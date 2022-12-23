import unittest
import os
from datetime import datetime
from entities.book_reference import BookReference
from services.reference_service import ReferenceService
from repositories.references_repository import ReferencesRepository
from tests.services.bibfile import bibfile
from bib_config import bib_test_file_path


class TestReferenceService(unittest.TestCase):
    def setUp(self):
        self.references_repository = ReferencesRepository()
        self.references_repository.delete_all_book_references()
        self.reference_service = ReferenceService(self.references_repository)
        self.book = BookReference("IDTEST", "Bergström, Gunilla",
                                  "Mikko Mallikas on oikukas", 1997, "Tammi", "Kontula", selected=True)
        self.reference_service.save_reference_to_db(self.book)
        self.time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        self.bibfile = bibfile()

    def test_save_book_db(self):
        result = self.reference_service.get_all_book_references_order_by_desc_datetime()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], self.book.author)

    def test_search_by_author(self):
        result = self.reference_service.references_search("Bergström, Gunilla")
        self.assertEqual(result[0][1], "Bergström, Gunilla")

    def test_search_returns_correct_value(self):
        result = self.reference_service.search("Bergström, Gunilla")
        correct = [("IDTEST", "Bergström, Gunilla",
                    "Mikko Mallikas on oikukas", 1997, "Tammi", "Kontula", 1)]
        self.assertEqual(result, correct)

    def test_search_keyword_not_found(self):
        result = self.reference_service.search("Halme, Toni")
        self.assertEqual(result, None)

    def test_all_references_are_returned_correctly(self):
        result = self.reference_service.search_all_ordered_by_descending_datetime()
        correct = [("IDTEST", "Bergström, Gunilla", "Mikko Mallikas on oikukas",
                    1997, "Tammi", "Kontula", 1, self.time)]
        self.assertEqual(result, correct)

    def test_if_no_references_are_found_return_none(self):
        self.references_repository.delete_all_book_references()
        result = self.reference_service.search_all_ordered_by_descending_datetime()
        self.assertEqual(result, None)

    def test_bib_generate_correctly(self):
        self.reference_service.create_bib_file()
        self.assertEqual(
            str(self.reference_service.read_bib_file()).strip(), str(self.book.bibtex))
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(
            basepath, bib_test_file_path()))
        os.remove(filepath) #muutos

    def test_fetch_all_book_references(self):
        self.book = BookReference("IDTEST2", "Bergström, Gunilla",
                                  "Mikko Mallikas on oikukas vai", 1996, "Tammi", "Kontula", selected=True)
        self.reference_service.save_reference_to_db(self.book)
        self.assertEqual(
            len(self.reference_service.fetch_all_book_references()), 2)

    def test_empty_show_selected_references_isnone(self):
        self.references_repository.delete_all_book_references()
        self.assertEqual(
            self.reference_service.show_selected_references(), None)

    def test_show_selected_references_hasselection(self):
        correct = [("IDTEST", "Bergström, Gunilla", "Mikko Mallikas on oikukas",
                    1997, "Tammi", "Kontula", 1, self.time)]
        self.assertEqual(self.reference_service.show_selected_references(), correct)


    def test_import_references_to_database(self):
        self.references_repository.delete_all_book_references()
        self.reference_service.import_references_from_bibfile(self.bibfile)
        data = self.reference_service.fetch_all_book_references()
        self.assertEqual(len(data), 2)
