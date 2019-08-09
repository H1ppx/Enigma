from __future__ import print_function, unicode_literals

import regex
from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))

class PermutationValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
            raise ValidationError(
                message='Please enter a string',
                cursor_position=len(document.text))
        except ValueError:
            if (len(list(document.text)) != len(set(list(document.text)))):
                raise ValidationError(
                    message='Repeats found, Please enter a valid permutation',
                    cursor_position=len(document.text)) 
            if (len(document.text) != 26):
                raise ValidationError(
                    message='Missing letters, Please enter a valid permutation',
                    cursor_position=len(document.text))
