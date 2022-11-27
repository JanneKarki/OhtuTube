class Io:
    def write(self, arg):
        print(arg)
        return

    def read(self,prompt=""):
            read = input(prompt)
            return read