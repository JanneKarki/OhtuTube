import unittest
from entities.book_reference import BookReference
from services.reference_service import reference_service
from repositories.references_repository import references_repository




class TestReferenceService(unittest.TestCase):
	def setUp(self):
		references_repository.delete_all_book_references()
		self.reference_service = reference_service
		self.book = BookReference("IDTEST", "Bergström, Gunilla", "Mikko Mallikas on oikukas", 1997, "Tammi", "Kontula")
		reference_service.save_reference_to_db(self.book)

	def test_save_book_db(self):
		result = self.reference_service.get_all_book_references()
		self.assertEqual(len(result), 1)
		self.assertEqual(result[0][1], self.book.author)

	def test_search_by_author(self):
		result = self.reference_service.search_by_author("Bergström, Gunilla")
		self.assertEqual(result.author, "Bergström, Gunilla")



