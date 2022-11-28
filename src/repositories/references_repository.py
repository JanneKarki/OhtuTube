from database_connection import get_database_connection


class ReferencesRepository:
    """Class for managing Book-references database.

    Attributes:
        connection: database-connection.
    """

    def __init__(self, connection):
        """Consturctor for the class.

        Args:
            connection (object): Database connection-object.
        """
        self.connection = connection

    def add_book_reference(self, book: object):
        """Adds book reference to the database.

        Args:
            author (str): Author of the book.
            title (str): Book title.
            year (int): Year when the book was published.
            publisher (str): Publisher of the book.

        """
        reference_id = book.reference_id
        author = book.author
        title = book.title
        year = book.year
        publisher = book.publisher
        address = book.address

        references_database = self.connection.cursor()

        references_database.execute(
            """INSERT INTO Books (
                    reference_id,
                    author,
                    title,
                    year,
                    publisher,
                    address
                    )
                    values (?,?,?,?,?,?)
                """,
            [reference_id, author, title, year, publisher, address]
        )

    def get_all_book_references_order_by_desc_datetime(self):
        """Gets and returns all book references sorted by descending datetime
            Returns:
                list: List of book references sorted by date
        """
        references_database = self.connection.cursor()

        references_database.execute(
            """SELECT
                reference_id,
                author,
                title,
                year,
                publisher,
                address,
                reference_datetime
                FROM Books
                ORDER BY reference_datetime DESC;
            """
        )

        results = references_database.fetchall()
        return results

    def get_book_references_by_search(self, search):
        """ Gets and returns all book references by a selected keyword.

        Args:
            search (str): Keyword to search.

        Returns:
            list: Returns a list of all book-references by keyword
        """

        references_database = self.connection.cursor()
        references_database.execute(
            """SELECT
                reference_id,
                author,
                title,
                year,
                publisher,
                address
                FROM Books
                WHERE
                author LIKE (CASE WHEN :search != '' THEN :search END)
                OR title LIKE (CASE WHEN :search != '' THEN :search END)
                OR year LIKE (CASE WHEN :search != '' THEN :search END)
                OR publisher LIKE (CASE WHEN :search != '' THEN :search END)
                OR address LIKE (CASE WHEN :search != '' THEN :search END)
                OR reference_id LIKE (CASE WHEN :search != '' THEN :search END)
                ORDER BY reference_datetime DESC;
            """,
            [f"%{search}%"]
        )
        results = references_database.fetchall()
        return results

    def delete_all_book_references(self):
        """ Removes all the book references from the database.
        """
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM Books")

        self.connection.commit()


references_repository = ReferencesRepository(get_database_connection())
