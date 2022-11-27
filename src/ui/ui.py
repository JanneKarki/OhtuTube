from services.reference_service import ReferenceService    
from ui.io import Io

COMMANDS = ("""Commands:
[1]Add new reference
[2]Display all references
[3]Search
[0]Exit""")


class Ui:
    """Class responsible for UI"""

    def __init__(self,io=Io()):
        "Initialize UI"
        self.methods = {
            1: self.display_add_reference, 
            2: self.display_search_book_by_desc_datetime,
            3: self.display_search_book,
            0: self.end
            }
        self.running = False
        self.services = ReferenceService(io)
        self.id = ""
    
    def start(self):
        self.running = True
        self.io.write("Welcome to the OhtuTube reference application \n")
        self.menu_loop()

    def display_menu(self):
        print("")
        print(COMMANDS)
        return self.menu_input()

    def menu_input(self):
        while True:
            print("")
            command = input()
            if command == "0":
                return 0
            elif command == "1":
                return 1
            elif command == "2":
                return 2
            elif command == "3":
                return 3
            print("Command not recognized, please enter a valid command")

    def menu_loop(self):
        """Basic menu loop functionality. Always returns to this"""
        while self.running:
            command = self.display_menu()
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
        return result
    
    def display_search_book_by_desc_datetime(self):
        result = self.services.search_all_ordered_by_descending_datetime()
        return result

    def confirm_entry(self, book):
        """Prints the entry attributes for user see and confirm
            before sending to the database"""
        while True:
            self.services.print_book_summary()
            print(book)
            answer = input(
                "Do you want to save this item to database? (y/n): ")
            if answer == "y":
                self.services.save_reference_to_db(book)
                status = "Failed to add!"
                info = self.services.get_all_book_references_order_by_desc_datetime()
                if self.id in info[0]:
                    status = "Added successfully!"
                return print(status)
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
        self.id = reference_id

        return self.services.set_book(
            reference_id, author, title, year, publisher, address)


    
    def end(self):
        print("\nClosing application")
        self.running = False
        return

    def stub(self):
        pass

# ui = Ui()
# ui.start()
