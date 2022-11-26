from ui.ui_menu import Menu
from services.reference_service import ReferenceService    

class Ui:
    """Class responsible for UI"""

    def __init__(self):
        "Initialize UI"
        self.methods = {
            1: self.display_add_reference,
            0: self.end
            }
        self.running = False
        self.services = ReferenceService()
    
    def start(self):
        self.running = True
        print("Welcome to the OhtuTube reference application \n")
        self.menu_loop()
    
    def menu_loop(self):
        """Basic menu loop functionality. Always returns to this"""
        while self.running:
            command = Menu().display_menu()
            self.methods[command]()

    def display_add_reference(self):
        """Collects entry inputs from the user, 
           confirms the entry before saving, 
           sends the reference object to the database.  
        """
        self.services.collect_inputs()
        self.services.confirm_entry()
        self.services.save_reference_to_db()

    
    def end(self):
        print("\nClosing application")
        self.running = False
        return

# ui = Ui()
# ui.start()