from services.generate_reference_id import GenerateReferenceID
from re import search


COMMANDS = ("""Commands:
[1]Add new reference
[2]Display all references
[3]Search
[4]Display selected references
[5]Create .bib file from selected references
[0]Exit""")


class Ui:
    """Class responsible for UI"""

    def __init__(self, io, services):
        "Initialize UI"
        self.io = io
        self.methods = {
            1: self.display_add_reference, 
            2: self.display_search_book_by_desc_datetime,
            3: self.display_search_book,
            4: self.display_selected_references,
            5: self.generate_bib_file,
            0: self.end
            }
        self.running = False
        self.services = services
        self.generate_ref_id = GenerateReferenceID()
        self.id = ""
    
    def start(self):
        self.running = True

        self.io.write("\n Welcome to the OhtuTube reference application \n")
        self.menu_loop()

    def display_menu(self):
        self.io.write(COMMANDS)
        return self.menu_input()

    def menu_input(self):
        while True:
            command = self.io.read("")
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
            self.io.write("Command not recognized, please enter a valid command")

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
        """Display all book references by keyword input"""
        author = self.io.read("> Keyword: ")
        result = self.services.search(author)
        return result

    def display_selected_references(self):
        """Display all selected references"""
        self.services.show_selected_references()
    
    def generate_bib_file(self):
        """Creates Bibtex file from selected references"""
        self.services.create_bib_file()

    def display_search_book_by_desc_datetime(self):
        """Display all book references ordered by time of creation"""
        result = self.services.search_all_ordered_by_descending_datetime()
        return result

    def confirm_entry(self, book):
        """Prints the entry attributes for user see and confirm
            before sending to the database"""
        while True:
            print(self.services.print_book_attr_titles())
            self.io.write(book)
            answer = self.io.read(
                "\n Do you want to save this item to database? (y/n): ")
            if answer == "y":
                self.services.save_reference_to_db(book)
                status = "Failed to add!"
                info = self.services.get_all_book_references_order_by_desc_datetime()
                if info:
                    if self.id in info[0]:
                        status = "Added successfully!"
                    return self.io.write(status)
            if answer == "n":
                print("\n")
                break
            self.io.write("Answer y(yes) or n(no)")

    def collect_inputs(self):
        """Collects entry inputs from the user and check if the 
            input is valid and informs if the input is not valid"""
        self.services.print_add_reference_title()

        reference_ids = {}
        for reference in self.services.get_all_book_references_order_by_desc_datetime():
            if reference[0] not in reference_ids: reference_ids[reference[0]] = reference

        while True:
            author = self.io.read("> Author (Last name, First name): ")
            if self.author_is_valid(author):
                break
            else:
                self.io.write("Error, enter the author like this: Bond, James")

        while True:
            title = self.io.read("> Title: ")
            if self.title_is_valid(title):
                break
            else:
                self.io.write("Error, field is empty!")

        while True:
            year = self.io.read("> Year: ")
            if self.year_is_valid(year):
                break
            else:
                self.io.write("Error, enter the year like this: 2014")

        while True:
            publisher = self.io.read("> Publisher: ")
            if self.publisher_is_valid(publisher):
                break
            else:
                self.io.write("Error, field is empty!")
            
        while True:
            address = self.io.read("> Address: ")
            if self.address_is_valid(address):
                break
            else:
                self.io.write("Error, field is empty!")

        info = self.services.search_all_ordered_by_descending_datetime()
        reference_id = self.generate_ref_id.generate_reference_id(author,year,title,info)

        self.id = reference_id
        return self.services.set_book(
            reference_id, author, title, year, publisher, address)

    def author_is_valid(self, author):
        if search(",", author):
            copy = author.split(",")
            for i in copy:
                if i.isspace() or i == "":
                    return False
            return True

    def title_is_valid(self, title):
        if title == "" or title.isspace():
            return False
        return True

    def year_is_valid(self, year):
        if year.isnumeric() and len(year) == 4 and year != "":
            return True
        return False

    def publisher_is_valid(self, publisher):
        if publisher == "" or publisher.isspace():
            return False
        return True

    def address_is_valid(self, address):
        if address == "" or address.isspace():
            return False
        return True
        

    def id_is_unique(self, id):
        info = self.services.get_all_book_references_order_by_desc_datetime()
        if not info:
            return True
        else:
            if id.isspace() or id == "":
                return False
            for references in info:
                if references[0] == id:
                    return False
        return True
            
    
    def end(self):
        self.io.write("\n Closing application")
        self.running = False
        return
