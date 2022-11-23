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

    def add_book_reference(self, author, title, year, publisher):
        """Adds book reference to the database.

        Args:
            author (str): Author of the book.
            title (str): Book title.
            year (int): Year when the book was published.
            publisher (str): Publisher of the book.

        """
        references_database = self.connection.cursor()

        references_database.execute(
                """INSERT INTO Books (
                    author,
                    title,
                    year,
                    publisher
                    )
                    values (?,?,?,?)
                """,
            [author, title, year, publisher]
        )

    def get_all_book_references(self):
        """ Gets and returns all the book-references from the database.

        Returns:
            list: Returns a list of all book-references
        """

        references_database = self.connection.cursor()

        references_database.execute(
            """SELECT
                author,
                title,
                year,
                publisher
                FROM Books
            """
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
