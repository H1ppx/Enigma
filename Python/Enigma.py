from Python.Components.Plugboard import Plugboard
from Python.Components.Rotor import Rotor
from Python.Components.Reflector import Reflector


class Enigma:

    def __init__(self, rotorAlphabetL, rotorAlphabetM, rotorAlphabetR):
        self.plugboard = Plugboard()
        self.rotorSlow = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO",1)
        self.rotorMed = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE",1)
        self.rotorFast = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ",1)
        self.reflector = Reflector()

    def run(self, text):
        text = text.upper()
        output = ""
        for c in text:
            temp = ""
            # Plugboard 1st Calc
            temp = self.plugboard.calc(c)

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

        return output


test = Enigma("abc", "def", "ghi")
print(test.run(input("Text \n")))
