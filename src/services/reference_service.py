from entities.book_reference import BookReference
from repositories.references_repository import (
    references_repository as default_references_repository
)
class ReferenceService:
    """ Application logic """
    def __init__(
        self,
        references_repository=default_references_repository
        ):

        self._references_repository = references_repository

    # missä muodossa lähdetiedot tulevat? JSON vaikka & json.loads() T.Esa
    def create_reference(self, entry_content ):
        """Creates a new book reference.

        Args:
            entry_content:
        Returns:
            Created a book reference in form of a BookReference object.
        """
        reference_id = entry_content.author
        author = entry_content.author
        year = entry_content.author
        title = entry_content.title
        publisher = entry_content.publisher
        book = BookReference(reference_id, author, title, year, publisher)
        #ja lähtevätkö ne tietokantaan kans yhdessä muodossa? siellä ne tuli erikseen
        return self._references_repository.add_book_reference(book)
reference_service = ReferenceService()
