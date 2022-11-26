class Menu:
    def __init__(self,io):
        self.io = io
    
    def display_menu(self):
        self.io.write("""Commands:
[1]Add new reference
[2]Search reference by author
[0]Exit""")
        return self.menu_input()

    def menu_input(self):
        while True:
            print("")
            command = self.io.read()
            if command == "0":
                return 0
            elif command == "1":
                return 1
            elif command == "2":
                return 2
            print("Command not recognized, please enter a valid command")