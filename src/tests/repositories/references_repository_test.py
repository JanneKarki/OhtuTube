import unittest
from repositories.references_repository import ReferencesRepository
from entities.book_reference import BookReference

class TestReferencesRepository(unittest.TestCase):
    def setUp(self):
        self.references_repository = ReferencesRepository()
        self.references_repository.delete_all_book_references()
        
        book = BookReference("IDTEST", "Bergström, Gunilla", "Mikko Mallikas on oikukas", 1997, "Tammi", "Kontula")
        self.references_repository.add_book_reference(book)

    def test_number_of_records_in_books_is_correct(self):
        data = self.references_repository.get_all_book_references_order_by_desc_datetime()
        self.assertEqual(len(data),1)