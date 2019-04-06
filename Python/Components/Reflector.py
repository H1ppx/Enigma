class Reflector:

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    permutation = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

    def calc(self, c):
        return self.permutation[self.alphabet.index(c)]
