from ui.language_display import english_display as en
from ui.language_display import finnish_display as fi

class ConsoleIO:
    def __init__(self):
        self._language = en

    def write(self, value):
        try:
            print(self._language[value]),
        except KeyError:
            print(value)

    def read(self, prompt):
        input_value = None
        try:
            input_value = input(self._language[prompt])
        except KeyError:
            input_value = input(prompt)
        return input_value

    def change_language(self):
        if self._language == en:
            self._language = fi
        else:
            self._language = en
