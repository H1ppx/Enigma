from Python.Components.Plugboard import Plugboard
from Python.Components.Rotor import Rotor
from Python.Components.Reflector import Reflector


class Enigma:

    def __init__(self, rotorAlphabetFast, rotorRotationFast, rotorAlphabetMed, rotorRotationMed, rotorAlphabetSlow, rotorRotationSlow):
        self.plugboard = Plugboard()
        self.rotorFast = Rotor(rotorAlphabetFast, rotorRotationFast)
        self.rotorMed = Rotor(rotorAlphabetMed, rotorRotationMed)
        self.rotorSlow = Rotor(rotorAlphabetSlow, rotorRotationSlow)
        self.reflector = Reflector()

    def printDayKey(self):
        print("Rotor Fast Alphabet: " + self.rotorFast.permutation)
        print("Rotor Med Alphabet: " + self.rotorMed.permutation)
        print("Rotor Slow Alphabet: " + self.rotorSlow.permutation)
        print("Plugboard: " + ''.join(self.plugboard.key1) + ", " + ''.join(self.plugboard.key2))

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


test = Enigma("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 0, "AJDKSIRUXBLHWTMCQGZNPYFVOE", 0, "BDFHJLCPRTXVZNYEIWGAKMUSQO", 0)
# print(test.run(input("Enter Text: \n")))
test.printDayKey()

