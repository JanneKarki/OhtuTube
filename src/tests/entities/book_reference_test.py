import unittest
from src.entities.book_reference import BookReference

class TestBookReference(unittest.TestCase):
    def setUp(self):
        self.author = "Bob"
        self.reference_id = "None"
        self.title = "This is the title"
        self.year = 1995
        self.publisher = "Helvette"
        self.book = BookReference(self.reference_id, self.author, self.title, self.year, self.publisher)

    def test_author_getter(self):
        author = self.book.author
        self.assertEqual(self.author, author)
    
    def test_author_setter(self):
        self.book.author("Dan")
        author = self.book.author
        self.assertEqual(author, "Dan")
        
    