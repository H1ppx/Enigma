from Python.Components.Plugboard import Plugboard
from Python.Components.Rotor import Rotor
from Python.Components.Reflector import Reflector


class Enigma:

    def __init__(self, rotorAlphabetFast, rotorAlphabetMed, rotorAlphabetSlow):
        self.plugboard = Plugboard()
        self.rotorFast = Rotor(rotorAlphabetFast, 0)
        self.rotorMed = Rotor(rotorAlphabetMed, 0)
        self.rotorSlow = Rotor(rotorAlphabetSlow, 0)
        self.reflector = Reflector()

    def run(self, text):
        text = text.upper()
        output = ""
        for c in text:
            temp = c

            # Plugboard 1st Calc
            temp = self.plugboard.calc(temp)
            # print(temp)

            # Fast Rotor 1st Calc
            temp = self.rotorFast.calc(temp, False)
            # print(temp)

            # Med Rotor 1st Calc
            temp = self.rotorMed.calc(temp, False)
            # print(temp)

            # Slow Rotor 1st Calc
            temp = self.rotorSlow.calc(temp, False)
            # print(temp)

            # Reflector
            temp = self.reflector.calc(temp)
            # print(temp)

            # Slow Rotor 2nd Calc
            temp = self.rotorSlow.calc(temp, True)
            # print(temp)

            # Med Rotor 1st Calc
            temp = self.rotorMed.calc(temp, True)
            # print(temp)

            # Fast Rotor 1st Calc
            temp = self.rotorFast.calc(temp, True)
            # print(temp)

            # Plugboard 2nd Calc
            temp = self.plugboard.calc(temp)
            # print(temp)

            # Add to Output
            output += temp

            # Rotate Motor
            if self.rotorFast.rotate() == 0:
                if self.rotorMed.rotate() == 0:
                    self.rotorSlow.rotate()

        return output


test = Enigma("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO")
print(test.run(input("Text \n")))
