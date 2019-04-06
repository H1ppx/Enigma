class Plugboard:

    def __init__(self):
        self.key1 = ['M', 'G', 'E', 'K', 'H', 'L']
        self.key2 = ['V', 'Y', 'C', 'N', 'R', 'P']

    def calc(self, c):
        if c in self.key1:
            return self.key2[self.key1.index(c)]
        elif c in self.key2:
            return self.key1[self.key2.index(c)]
        else:
            return c
