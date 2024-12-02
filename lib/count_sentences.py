#!/usr/bin/env python3

class MyString:

    def __init__(self, value=''):
        self.value = value  # Calls the setter to validate input

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        cleaned_value = self.value.replace('!', '.').replace('?', '.')
        sentences = cleaned_value.split('.')
        return len([sentence for sentence in sentences if sentence.strip()])

