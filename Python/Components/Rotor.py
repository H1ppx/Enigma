"""
The rotor class replicates the physical rotor in an Enigma.
"""


class Rotor:

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    amountOfRotations = 0

    def __init__(self, permutation, rotation):
        """
        :param permutation: string, mono-alphabetic permutation of the alphabet in string form with corresponding
            alphabet going from A-Z i.e. EKMFLGDQVZNTOWYHXUSPAIBRCJ
        :param rotation: int, rotation that the rotor starts in
        """
        self.permutation = permutation
        self.rotation = rotation

    def calc(self, c, reflected):
        """
        :param c: char, character being encrypted or decrypted
        :param reflected: boolean, Whether the character has been reflected
        :return: char, post-encryption/decryption character
        """
        if reflected:
            return self.alphabet[(self.permutation.find(c) + self.rotation) % 26]
        else:
            return self.permutation[(self.alphabet.find(c) - self.rotation) % 26]

    def rotate(self):
        """
        :return: new current rotation
        """
        self.rotation += 1
        self.amountOfRotations += 1
        return self.amountOfRotations % 26
