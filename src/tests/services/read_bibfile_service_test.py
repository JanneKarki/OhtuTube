import unittest
from services.read_bibfile_service import ReadBibfileService



BIBFILE = """@book{mcg2021,
        author = {"Metz, Cade"},
        title = {"Genius Makers"},
        year = {"2021"},
        publisher = {"Penguin"},
        address = {"London"}
        }
@book{ecb18,
        author = {"Evans, Claire"},
        title = {"Broad band"},
        year = {"2018"},
        publisher = {"Portfolio/Penguin"},
        address = {"New York"}
        }
		"""


class TestReadBibfileService(unittest.TestCase):
	def setUp(self):
		self.read_bibfile_service = ReadBibfileService()

	
	def test_read_first_reference_id(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[0][0], "mcg2021")

	def test_read_first_reference_author(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[0][1], "Metz, Cade")

	def test_read_first_reference_title(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[0][2], "Genius Makers")
	
	def test_read_first_reference_year(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[0][3], "2021")
	
	def test_read_first_reference_publisher(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[0][4], "Penguin")

	def test_read_first_reference_address(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[0][5], "London")
	
	def test_read_second_reference_id(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[1][0], "ecb18")

	def test_read_second_reference_author(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[1][1], "Evans, Claire")

	def test_read_second_reference_title(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[1][2], "Broad band")

	def test_read_second_reference_year(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[1][3], "2018")

	def test_read_second_reference_publisher(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[1][4], "Portfolio/Penguin")

	def test_read_second_reference_address(self):
		references = self.read_bibfile_service.decode_bibfile(BIBFILE)
		self.assertEqual(references[1][5], "New York")