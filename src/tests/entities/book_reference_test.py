import unittest
from entities.book_reference import BookReference

class TestBookReference(unittest.TestCase):
    def setUp(self):
        self.author = "Bob"
        self.reference_id = "None"
        self.title = "This is the title"
        self.year = 1995
        self.publisher = "Helvette"
        self.book = BookReference(self.reference_id, self.author, self.title, self.year, self.publisher)

    def test_author_getter(self):
        fetched_author = self.book.author
        self.assertEqual(self.author, fetched_author)
    
    def test_author_setter(self):
        self.book.author = "Dan"
        fetched_author = self.book.author
        self.assertEqual(fetched_author, "Dan")
    
    def test_reference_id_getter(self):
        fetched_reference_id = self.book.reference_id
        self.assertEqual(fetched_reference_id, self.reference_id)
    
    def test_reference_id_setter(self):
        self.book.reference_id = "123AD"
        fetched_reference_id = self.book.reference_id
        self.assertEqual(fetched_reference_id, "123AD")
    
    
    def test__str__call(self):
        self.assertEqual(self.book.__str__(), f"{self.author:20} | {self.title:20} | {self.year:5} | {self.publisher:20}")

    