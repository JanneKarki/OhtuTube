from ui.ui_menu import Menu
from services.reference_service import ReferenceService    
from ui.io import Io

class Ui:
    """Class responsible for UI"""

    def __init__(self,io=Io()):
        "Initialize UI"
        self.methods = {
            1: self.display_add_reference,
            2: self.display_search_book_by_author,
            0: self.end
            }
        self.running = False
        self.services = ReferenceService(io)
        self.menu = Menu(io)
        self.io = io
    
    def start(self):
        self.running = True
        self.io.write("Welcome to the OhtuTube reference application \n")
        self.menu_loop()
    
    def menu_loop(self):
        """Basic menu loop functionality. Always returns to this"""
        while self.running:
            command = self.menu.display_menu()
            self.methods[command]()

    def display_add_reference(self):
        """Collects entry inputs from the user, 
           confirms the entry before saving, 
           sends the reference object to the database.  
        """
        self.services.collect_inputs()
        self.services.confirm_entry()

    def display_search_book_by_author(self):
        """Display data by author inputs"""
        self.services.search_by_author()

    
    def end(self):
        print("\nClosing application")
        self.running = False
        return

    def stub(self):
        pass

# ui = Ui()
# ui.start()