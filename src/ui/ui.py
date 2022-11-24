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
        """Asks the user for information"""
        print("---------------------------------------------------------------------------------------------------------------")
        print("| If there are several authors or address, separate them with a comma like this: Example1, Example2, Example3 |")
        print("---------------------------------------------------------------------------------------------------------------")
        title = input("Title: ")
        author = input("Author: ")
        year = input("Year: ")
        publisher = input("Publisher: ")
        address = input("Address: ")
        while True:
            answer = input("Do you want to save to database? (y/n): ")
            # Not yet adding anything to the database and not tested
            if answer == "y":
                return
            if answer == "n":
                return
            else:
                print("Answer y(yes) or n(no)")
        pass
    
    def end(self):
        print("\nClosing application")
        self.running = False
        return

ui = Ui()
ui.start()