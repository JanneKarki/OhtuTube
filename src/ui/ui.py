from ui.ui_menu import Menu
from services.reference_service import ReferenceService    

class Ui:
    """Class responsible for UI"""

    def __init__(self):
        "Initialize UI"
        self.methods = {
            1: self.display_add_reference, 
            2: self.display_search_book_by_DESC_datetime,
            3: self.display_search_book,
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
        book = self.collect_inputs()
        self.confirm_entry(book)

    def display_search_book(self):
        """Display all book references by author inputs"""

        author = input("> Author (Last name, First name): ")
        result = self.services.search(author)

        print(result)
    
    def display_search_book_by_DESC_datetime(self):
        """Display all book references ordered by descending datetime
        """
        result = self.services.search_all_ordered_by_descending_datetime()
        print(result)

    def confirm_entry(self, book):
        """Prints the entry attributes for user see and confirm
            before sending to the database"""
        while True:
            self.services.print_book_summary()
            print(book)
            answer = input(
                "Do you want to save this item to database? (y/n): ")
            if answer == "y":
                return self.services.save_reference_to_db(book)
            if answer == "n":
                print("\n")
                break
            print("Answer y(yes) or n(no)")

    def collect_inputs(self):
        """Collects entry inputs from the user"""
        self.services.print_add_reference_title()

        author = input("> Author (Last name, First name): ")
        title = input("> Title: ")
        year = input("> Year: ")
        publisher = input("> Publisher: ")
        address = input("> Address: ")
        reference_id = input("> Create a unique reference id: ")

        return self.services.set_book(
            reference_id, author, title, year, publisher, address)


    
    def end(self):
        print("\nClosing application")
        self.running = False
        return

# ui = Ui()
# ui.start()