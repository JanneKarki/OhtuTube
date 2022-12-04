import unittest
from entities.book_reference import BookReference
from services.reference_service import ReferenceService
from services.generate_reference_id import GenerateReferenceID
from repositories.references_repository import ReferencesRepository

class TestGenerateReferenceID(unittest.TestCase):
    def setUp(self):
        self.references_repository = ReferencesRepository()
        self.reference_generator = GenerateReferenceID()
        self.reference_service = ReferenceService(self.references_repository)
        self.references_repository.delete_all_book_references()

    def test_reference_id_is_generated_correctly(self):
        author = "Orwell, George"
        year =  str(1949)
        title = "1984"
        info = self.reference_service.get_all_book_references_order_by_desc_datetime()
        generated_reference_id = self.reference_generator.generate_reference_id(author, year, title, info)
        correct_reference_id = "orwe19491984"
        self.assertEqual(generated_reference_id, correct_reference_id)

    def test_reference_id_is_already_in_the_db(self):
        book = BookReference("orwe19491984", "Orwell, George", "1984", 1949, "	Secker & Warburg", "UK")
        self.reference_service.save_reference_to_db(book)
        reference_id = "orwe19491984"
        info = self.reference_service.get_all_book_references_order_by_desc_datetime()
        is_duplicate = self.reference_generator.is_duplicate_reference_id(reference_id, info)
        self.assertEqual(is_duplicate, True)

    def test_add_random_string_if_reference_already_exists(self):
        book = BookReference("orwe19491984", "Orwell, George", "1984", 1949, "	Secker & Warburg", "UK")
        self.reference_service.save_reference_to_db(book)
        author = "Orwell, George"
        year =  str(1949)
        title = "1984"
        info = self.reference_service.get_all_book_references_order_by_desc_datetime()
        generated_reference_id = self.reference_generator.generate_reference_id(author, year, title, info)
        self.assertEqual(generated_reference_id, generated_reference_id)
