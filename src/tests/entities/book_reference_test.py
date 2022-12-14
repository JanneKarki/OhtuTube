import unittest
from entities.book_reference import BookReference


class TestBookReference(unittest.TestCase):
    def setUp(self):
        self.author = "Larman, Craig"
        self.reference_id = "larm2016larg"
        self.title = "Large-Scale Scrum"
        self.year = 2016
        self.publisher = "Addison-Wesley"
        self.address = "Reading"
        self.book = BookReference(
            self.reference_id,
            self.author,
            self.title,
            self.year,
            self.publisher,
            self.address,
        )

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
        bibtex_model = """@book{larm2016larg,
        author = {Larman, Craig},
        title = {Large-Scale Scrum},
        year = {2016},
        publisher = {Addison-Wesley},
        address = {Reading}
        }"""

        self.assertEqual(bibtex, bibtex_model)

    def test__str__call(self):
        self.assertEqual(
            str(self.book),
            f"    NO   | {self.reference_id:13} | {self.author:19} | {self.title:28} | "
            + f"{self.year:6} | {self.publisher:18} | {self.address:18}",
        )

    def test__str__call_with_exceeding_input(self):
        self.author = "Larman, Craig and Vodde, Bass"
        self.reference_id = "larm2016larg"
        self.title = "Large-Scale Scrum: More with LeSS"
        self.year = 2016
        self.publisher = "Addison-Wesley Publishings"
        self.address = "Reading, Massachusetts"

        self.book = BookReference(
            self.reference_id,
            self.author,
            self.title,
            self.year,
            self.publisher,
            self.address,
        )

        self.assertEqual(
            str(self.book),
            f"    NO   | {self.reference_id:13} | {self.author[0:16] + '...':19} | {self.title[:25] + '...':28} | "
            + f"{self.year:6} | {self.publisher[:15] + '...':18} | {self.address[:15] + '...':18}"
        )



