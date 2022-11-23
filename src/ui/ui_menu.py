class Menu:
    def display_menu(self):
        print("""Commands:
[1]Add new reference
[0]Exit""")
        return self.menu_input()

    def menu_input(self):
        while True:
            print("")
            command = input()
            if command == "0":
                return 0
            elif command == "1":
                return 1
            print("Command not recognized, please enter a valid command")