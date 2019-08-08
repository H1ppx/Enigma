class Reflector:

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, permutation):
        """
        :param permutation: string, mono-alphabetic permutation of the alphabet i.e. YRUHQSLDPXNGOKMIEBFZCWVJAT
        """
        self.permutation = permutation

    def calc(self, c):
        """
        Swaps character with corresponding letter in permuted alphabet
        :param c: char, character being encrypted or decrypted
        :return: char, post-encryption/decryption character
        """
        return self.permutation[self.alphabet.index(c)]
