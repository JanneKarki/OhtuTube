from ui.ui import Ui
from console_io import ConsoleIO
from repositories.references_repository import ReferencesRepository
from services.reference_service import ReferenceService

def main():
    references_repository = ReferencesRepository()
    _ui = Ui(ConsoleIO(), ReferenceService(references_repository))
    _ui.start()

if __name__ == "__main__":
    main()
