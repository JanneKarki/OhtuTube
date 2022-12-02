
class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def write(self, prompt):
        self.outputs.append(prompt)

    def add_input(self, value):
        self.inputs.append(value)
