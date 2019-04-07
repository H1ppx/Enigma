class Rotor:

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    amountOfRotations = 0

    def __init__(self, permutation, rotation):
        self.permutation = permutation
        self.rotation = rotation

    def calc(self, c, reflected):
        if reflected:
            return self.alphabet[(self.permutation.find(c) + self.rotation) % 26]
        else:
            return self.permutation[(self.alphabet.find(c) - self.rotation) % 26]

    def rotate(self):
        self.rotation += 1
        self.amountOfRotations += 1
        return self.amountOfRotations % 26
