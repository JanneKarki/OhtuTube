
class BookReference:
    """ Class for a single Book reference
    Attributes:
    """

    def __init__(self,
                 reference_id: str,
                 author: str,
                 title: str,
                 year: int,
                 publisher: str,
                 address: str,
                 selected=False
                 ):
        """Class constructor to create a new Book reference
        Args:
            author (str): Author of the book.
            title (str): Book title.
            year (int): Year when the book was published.
            publisher (str): Publisher of the book.
        """
        self._reference_id = reference_id
        self._author = author
        self._title = title
        self._year = year
        self._publisher = publisher
        self._address = address
        self._selected = selected

    @property
    def reference_id(self):
        """Method that returns reference id
        Returns:
            str: Reference id
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Method that sets reference id

        Args:
            reference_id (_type_): _description_
        """
        self._reference_id = reference_id

    @property
    def author(self):
        """Method that returns the author
        Returns:
            str: Author of the book
        """
        return self._author

    @author.setter
    def author(self, author):
        """Method that sets the author
        Args:
            author (str): Author of the book
        """
        self._author = author

    @property
    def title(self):
        """Method that returns the title
        Returns:
            str: Title of the book
        """
        return self._title

    @title.setter
    def title(self, title):
        """Method that sets the title
        Args:
            title (str): Title of the Book
        """
        self._title = title

    @property
    def year(self):
        """ Method that return the year
        Returns:
            int: Publication year
        """
        return self._year

    @year.setter
    def year(self, year):
        """Method that sets the year
        """
        self._year = year

    @property
    def publisher(self):
        """Method that returns the publisher
        Returns:
            str: Publisher of the book
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Method that sets the publisher

        Args:
            publisher (): _description_
        """
        self._publisher = publisher

    @property
    def address(self):
        """Method that return the address
        Returns:
            str:  Address of publication
        """
        return self._address

    @address.setter
    def address(self, address):
        """Method that sets the address
        """
        self._address = address

    @property
    def selected(self):
        """Methods that returns True if book reference is selected
        Returns:
            bool: True if book reference is selected
        """
        return self._selected

    @selected.setter
    def selected(self, selection_bool):
        """Method that sets selected True if book reference is selected"""
        self._selected = selection_bool

    @property
    def bibtex(self):
        """Method that returns bibtex form
        Returns:
            str: Bibtex form
        """

        return f"""@book{{{self.reference_id},
        author = {{{self.author}}},
        title = {{{self.title}}},
        year = {{{self.year}}},
        publisher = {{{self.publisher}}},
        address = {{{self.address}}}
        }}"""

    def __str__(self):
        """Method that returns reference in styled form
        Returns:
            str: Styled reference form
        """

        if len(self.author) > 19:
            self.author = self.author[0:16] + '...'
        if len(self._title) > 19:
            self.title = self.title[:25] + '...'
        if len(self._publisher) > 19:
            self.publisher = self.publisher[:15] + '...'
        if len(self.address) > 19:
            self.address = self.address[:15] + '...'

        if self._selected:
            return (
                f"   YES   | {self.reference_id:13} | {self.author:19} | {self.title:28} | " +
                f"{self.year:6} | {self.publisher:18} | {self.address:18}"
            )
        return (
            f"    NO   | {self.reference_id:13} | {self.author:19} | {self.title:28} | " +
            f"{self.year:6} | {self.publisher:18} | {self.address:18}"
        )
