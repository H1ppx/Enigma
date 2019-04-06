class Rotor:

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, permutation, position):
        self.permutation = permutation
        self.position = position

    def calc(self, c, reflected):
        if reflected:
            return self.alphabet[self.permutation.find(c)]
        else:
            return self.permutation[self.alphabet.find(c)]

    def rotate(self):
        self.shifts
        # TODO
