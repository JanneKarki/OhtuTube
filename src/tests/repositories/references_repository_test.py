import unittest
from repositories.references_repository import references_repository
from entities.book_reference import BookReference

class TestReferencesRepository(unittest.TestCase):
    def setUp(self):
        references_repository.delete_all_book_references()
        self.references_repository = references_repository
        book = BookReference("IDTEST", "Bergström, Gunilla", "Mikko Mallikas on oikukas", 1997, "Tammi")
        references_repository.add_book_reference(book)   

    def test_number_of_records_in_books_is_correct(self):
        data = self.references_repository.get_all_book_references()
        self.assertEqual(len(data),1)
