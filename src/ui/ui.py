from re import search
from services.reference_service import ReferenceService    

COMMANDS = ("""Commands:
[1]Add new reference
[2]Display all references
[3]Search
[4]Display selected references
[5]Create .bib file from selected references
[0]Exit""")


class Ui:
    """Class responsible for UI"""

    def __init__(self):
        "Initialize UI"
        self.methods = {
            1: self.display_add_reference, 
            2: self.display_search_book_by_desc_datetime,
            3: self.display_search_book,
            0: self.end
            }
        self.running = False
        self.services = ReferenceService()
        self.id = ""
    
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
            elif command == "3":
                return 3
            elif command == "4":
                return 4
            elif command == "5":
                return 5
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
    
    def display_selected_references():
        

    def display_search_book(self):
        """Display all book references by keyword input"""
        author = input("> Keyword: ")
        result = self.services.search(author)
        return result
    
    def display_search_book_by_desc_datetime(self):
        """Display all book references ordered by time of creation"""
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
        """Collects entry inputs from the user and check if the 
            input is valid and informs if the input is not valid"""
        self.services.print_add_reference_title()

        reference_ids = {}
        for reference in self.services.get_all_book_references_order_by_desc_datetime():
            if reference[0] not in reference_ids: reference_ids[reference[0]] = reference

        while True:
            author = input("> Author (Last name, First name): ")
            status = False
            if search(",", author):
                copy = author.split(",")
                for i in copy:
                    if i.isspace() or i == "":
                        status = False
                        break
                    else:
                        status = True
            if status == True:
                break
            print("Error, enter the author like this: Bond, James")

        while True:
            title = input("> Title: ")
            if title == "" or title.isspace() or title.isspace():
                print("Error, field is empty!")
            else:
                break

        while True:
            year = input("> Year: ")
            if year.isnumeric() and len(year) == 4 and year != "":
                break
            print("Error, enter the year like this: 2014")

        while True:
            publisher = input("> Publisher: ")
            if publisher == "" or publisher.isspace():
                print("Error, field is empty!")
            else:
                break

        while True:
            address = input("> Address: ")
            if address == "" or address.isspace():
                print("Error, field is empty!")
            else:
                break

        while True:
            
            reference_id = input("> Create a unique reference id: ")
            stat = True
            if reference_id.isspace():
                stat = False
            if stat == True and reference_id != "" and reference_id:
                if reference_id in reference_ids:
                            print("Error, field is empty or id already taken!")
                else: break
            

        self.id = reference_id
        return self.services.set_book(
            reference_id, author, title, year, publisher, address)
    
    def end(self):
        print("\nClosing application")
        self.running = False
        return

# ui = Ui()
# ui.start()
