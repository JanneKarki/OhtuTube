class StubIo:
    def __init__(self):
        self.last_arg = None
        self.command = "x"

    def write(self, arg):
        self.last_arg = arg
        return

    def read(self,prompt=""):
            if self.command != "x":
                self.command == "x"
            return self.command