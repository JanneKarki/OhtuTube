
class BookReference:
    """ Class for a single Book reference 
    
    Attributes:
    
    """

    def __init__(self, author, title, year, publisher):
        """Class constructor to create a new Book reference 
        
        Args:
            author (str): Author of the book.
            title (str): Book title.
            year (int): Year when the book was published.
            publisher (str): Publisher of the book.
        """

        self.author = author
        self.title = title
        self.year = year
        self.publisher = publisher

    # käytetäänkö tässä versiossa esim kirjan nimeä id:nä?
