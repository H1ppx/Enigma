from __future__ import print_function, unicode_literals

from Components.Plugboard import Plugboard
from Components.Rotor import Rotor
from Components.Reflector import Reflector
from Components.Utils import NumberValidator, PermutationValidator

from tabulate import tabulate
import random
import numpy as np
from pyfiglet import Figlet
from PyInquirer import style_from_dict, Token, prompt, Separator, print_json
from pprint import pprint

import os


'''
//TODO Docs

'''

class Enigma:

    def __init__(self, rotorAlphabetFast, rotorRotationFast, rotorAlphabetMed, rotorRotationMed, rotorAlphabetSlow, rotorRotationSlow, reflectorPermutation):
        self.plugboard = Plugboard()
        self.rotorFast = Rotor(rotorAlphabetFast, rotorRotationFast)
        self.rotorMed = Rotor(rotorAlphabetMed, rotorRotationMed)
        self.rotorSlow = Rotor(rotorAlphabetSlow, rotorRotationSlow)
        self.reflector = Reflector(reflectorPermutation)

    def printDayKey(self):
        print("Rotor Fast Alphabet: " + self.rotorFast.permutation)
        print("Rotor Med Alphabet: " + self.rotorMed.permutation)
        print("Rotor Slow Alphabet: " + self.rotorSlow.permutation)
        print("Plugboard:")
        print((list(zip(self.plugboard.key1, self.plugboard.key2))))

    def run(self, text):
        text = text.upper()
        text = text.replace(" ", "")
        output = ""
        for c in text:
            temp = c

            # Plugboard 1st Calc
            temp = self.plugboard.calc(temp)

            # Fast Rotor 1st Calc
            temp = self.rotorFast.calc(temp, False)

            # Med Rotor 1st Calc
            temp = self.rotorMed.calc(temp, False)

            # Slow Rotor 1st Calc
            temp = self.rotorSlow.calc(temp, False)

            # Reflector
            temp = self.reflector.calc(temp)
            
            # Slow Rotor 2nd Calc
            temp = self.rotorSlow.calc(temp, True)

            # Med Rotor 1st Calc
            temp = self.rotorMed.calc(temp, True)

            # Fast Rotor 1st Calc
            temp = self.rotorFast.calc(temp, True)

            # Plugboard 2nd Calc
            temp = self.plugboard.calc(temp)

            # Add to Output
            output += temp

            # Rotate Motor
            if self.rotorFast.rotate() == 0:
                if self.rotorMed.rotate() == 0:
                    self.rotorSlow.rotate()

        return output

class Ui:

    def genRndPerm(self): 
        return ''.join(np.random.permutation(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")))


    def run(self):
        os.system('cls')
        f = Figlet(font='slant')
        print(f.renderText('Enigma'))

        settingQuestions = [
            {
                'type': 'list',
                'name': 'Enigma Settings',
                'message': 'Enigma Settings',
                'choices': ['Create new enigma w/ custom settings', 
                    'Create new enigma w/ rnd settings'
                    ],
                'filter': lambda val: val.lower()
            }
        ]

        settingAnswers = prompt(settingQuestions)

        if (settingAnswers == {'Enigma Settings': 'create new enigma w/ custom settings'}):
            customQuestions = [
                {
                    'type': 'input',
                    'name': 'a',
                    'message': 'Fast Rotor Permutation:',
                    'validate': PermutationValidator
                },
                {   
                    'type': 'input',
                    'name': 'b',
                    'message': 'Fast Rotor Starting Position:',
                    'validate': NumberValidator,
                    'filter': lambda val: int(val)
                },
                {
                    'type': 'input',
                    'name': 'c',
                    'message': 'Medium Rotor Permutation:',
                    'validate': PermutationValidator
                },
                {   
                    'type': 'input',
                    'name': 'd',
                    'message': 'Medium Rotor Starting Position:',
                    'validate': NumberValidator,
                    'filter': lambda val: int(val)
                },
                {
                    'type': 'input',
                    'name': 'e',
                    'message': 'Fast Rotor Permutation:',
                    'validate': PermutationValidator
                },
                {   
                    'type': 'input',
                    'name': 'f',
                    'message': 'Slow Rotor Starting Position:',
                    'validate': NumberValidator,
                    'filter': lambda val: int(val)
                },
                {
                    'type': 'input',
                    'name': 'g',
                    'message': 'Reflector Permutation:',
                    'validate': PermutationValidator
                }
            ]

            answers = prompt(customQuestions)
            enigma = Enigma(answers.get('a'), answers.get('b'),
                answers.get('c'), answers.get('d'),
                answers.get('e'), answers.get('f'),
                answers.get('g'))

        elif (settingAnswers == {'Enigma Settings': 'create new enigma w/ rnd settings'}):
            enigma = Enigma(self.genRndPerm(), 0,
                self.genRndPerm(), 0, 
                self.genRndPerm(), 0, 
                self.genRndPerm())


        enigma.printDayKey()
        print(enigma.run(input("Enter Text: \n")))

ui = Ui()
ui.run()           


