
class BookReference:
    """ Class for a single Book reference 

    Attributes:

    """

    def __init__(self, reference_id, author, title, year, publisher):
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

    def __str__(self):
        """Method that returns reference in styled form
        Returns:
            str: Styled reference form
        """
        return f"{self._author:20} | {self._title:20} | {self._year:5} | {self._publisher:20} "