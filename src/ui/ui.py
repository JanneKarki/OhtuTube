from services.reference_service import ReferenceService    

COMMANDS = ("""Commands:
[1]Add new reference
[2]Search reference by author
[0]Exit""")


class Ui:
    """Class responsible for UI"""

    def __init__(self):
        "Initialize UI"
        self.methods = {
            1: self.display_add_reference,
            2: self.display_search_book_by_author,
            0: self.end
            }
        self.running = False
        self.services = ReferenceService()
    
    def start(self):
        self.running = True
        print("")
        print("Welcome to the OhtuTube reference application \n")
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

    def display_search_book_by_author(self):
        """Display data by author inputs"""

        author = input("> Author (Last name, First name): ")

        result = self.services.search_by_author(author)

        return result

    def confirm_entry(self, book):
        """Prints the entry attributes for user see and confirm
            before sending to the database"""
        while True:

            self.services.print_book_summary(book)
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