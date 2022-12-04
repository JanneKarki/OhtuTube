import unittest
from datetime import datetime
from entities.book_reference import BookReference
from services.reference_service import ReferenceService
from repositories.references_repository import ReferencesRepository




class TestReferenceService(unittest.TestCase):
	def setUp(self):
		self.references_repository = ReferencesRepository()
		self.references_repository.delete_all_book_references()
		self.reference_service = ReferenceService(self.references_repository)
		self.book = BookReference("IDTEST", "Bergström, Gunilla", "Mikko Mallikas on oikukas", 1997, "Tammi", "Kontula")
		self.reference_service.save_reference_to_db(self.book)
		self.time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

	def test_save_book_db(self):
		result = self.reference_service.get_all_book_references_order_by_desc_datetime()
		self.assertEqual(len(result), 1)
		self.assertEqual(result[0][1], self.book.author)

	def test_search_by_author(self):
		result = self.reference_service.references_search("Bergström, Gunilla")
		self.assertEqual(result[0][1], "Bergström, Gunilla")

	def test_search_returns_correct_value(self):
		result = self.reference_service.search("Bergström, Gunilla")
		correct = [("IDTEST", "Bergström, Gunilla", "Mikko Mallikas on oikukas", 1997, "Tammi", "Kontula", 0)]
		self.assertEqual(result, correct)

	def test_search_keyword_not_found(self):
		result = self.reference_service.search("Halme, Toni")
		result = self.assertEqual(result, None)

	def test_all_references_are_returned_correctly(self):
		result = self.reference_service.search_all_ordered_by_descending_datetime()
		correct = [("IDTEST", "Bergström, Gunilla", "Mikko Mallikas on oikukas", 1997, "Tammi", "Kontula", 0, self.time)]
		self.assertEqual(result, correct)
	
	def test_if_no_references_are_found_return_none(self):
		self.references_repository.delete_all_book_references()
		result = self.reference_service.search_all_ordered_by_descending_datetime()
		self.assertEqual(result, None)
