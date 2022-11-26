from ui.stub_io import StubIo
from ui.ui import Ui

class AppLibrary:
    def __init__(self):
        self.ui = Ui(StubIo())
    
    def run_application(self):
        self.ui.start()
    
    def input_command(self, value):
        self.ui.io.command = str(value)
    

