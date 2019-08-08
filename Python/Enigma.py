from Components.Plugboard import Plugboard
from Components.Rotor import Rotor
from Components.Reflector import Reflector

from tabulate import tabulate
import random
import numpy as np

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
        print('\nEnigma \n')
        print(tabulate([['Create New Enigma w/ Custom Settings', 0], ['Create New Random Enigma w/ Rnd Settings', 1], ['Load Saved Enigma', 2]], headers=['Machine Settings', 'Enter Key'],  tablefmt="fancy_grid"))
        settingsInput = input('\nEnter: ')
        print("")


        if (settingsInput == '0'):
            print('Create New Enigma w/ Custom Settings\n')

            # TODO: Finish
        
    
        elif (settingsInput == '1'):
            print('Create New Random Enigma w/ Rnd Settings\n')
            enigma = Enigma(self.genRndPerm(), 0,
                self.genRndPerm(), 0, 
                self.genRndPerm(), 0, 
                self.genRndPerm())


        elif (settingsInput == '2'):
            print('Load Saved Enigma\n')
            # TODO: Get CSV save and Read
        
        enigma.printDayKey()
        print(enigma.run(input("Enter Text: \n")))

ui = Ui()
ui.run()           


