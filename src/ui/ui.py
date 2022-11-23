from ui_menu import Menu

class Ui:
    """Class responsible for UI"""

    def __init__(self):
        "Initialize UI"
        self.methods = {
            1: self.display_add_reference,
            0: self.end
            }
        self.running = False
    
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
        #todo
        pass
    
    def end(self):
        print("\nClosing application")
        self.running = False
        return

ui = Ui()
ui.start()