from ui.language_display import english_display as en
from ui.language_display import finnish_display as fi

class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []
        self._language = en

    def read(self, prompt):
        # pylint: disable=unused-argument
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def write(self, prompt):
        try:
            self.outputs.append(self._language[str(prompt)])
        except KeyError:
            self.outputs.append(str(prompt))

    def add_input(self, value):
        self.inputs.append(value)

    def change_language(self):
        if self._language == en:
            self._language = fi
        else:
            self._language = en
