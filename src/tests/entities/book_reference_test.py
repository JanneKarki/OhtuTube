import unittest
from entities.book_reference import BookReference

class TestBookReference(unittest.TestCase):
    def setUp(self):
        self.author = "Larman, Craig and Vodde, Bass"
        self.reference_id = "LESS"
        self.title = "Large-Scale Scrum: More with LeSS"
        self.year = 2016
        self.publisher = "Addison-Wesley"
        self.address = "Reading, Massachusetts"
        self.book = BookReference(self.reference_id, self.author, self.title, self.year, self.publisher, self.address)

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
    
    def test_bibtex(self):
        bibtex = self.book.bibtex
        bibtex_model = """@book{LESS,
        author = \"Larman, Craig and Vodde, Bass\",
        title = \"Large-Scale Scrum: More with LeSS\",
        year = \"2016\",
        publisher = \"Addison-Wesley\",
        address = \"Reading, Massachusetts\"
        }"""
        self.assertEqual(bibtex, bibtex_model)

    def test__str__call(self):
        self.assertEqual(self.book.__str__(), f"{self.author:30}|{self.title:30}|{self.year:5}|{self.publisher:20}|{self.address:30}")

    