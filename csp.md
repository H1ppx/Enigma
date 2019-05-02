# Create Task Written Response

## 2A

The program was written in python. The purpose of this program is to demonstrate encryption by an Enigma Machine. The 
program takes an input string and proceeds to run a 3-motor enigma machine encryption. The encryption is poly-alphabetic 
as after the encryption of a letter, one or more rotor rotates a step causing the permutation of the alphabet to 
change. The encryption by rotor is one-way and does not encrypt the same in both directions. A letter is 
encrypted in the following path: input -> plugboard -> rotor 1 -> rotor 2 -> rotor 3 -> reflector -> rotor 3 -> rotor 2 
-> rotor 1 -> plugboard -> output. Per encryption of a letter, rotor 1 rotates. When a rotor 'n' completes 26 rotations,
rotor 'n+1' rotates a step. The video shows the encryption and decryption of the phrase 'hello world'. When run, the 
following information will be printed: all rotor permutations of the alphabet and the plugboard substitutions.

## 2B
This project was completed independently. The programming of this project was done both incrementally and iteratively. I 
started by creating a flow chart of how the original enigma machine would encrypt and decrypt messages. Following this,
I physically created a model of how a human could manually encrypt and decrypt an Enigma. When I originally started 
writing the program I hard coded all components and processes for the encryption in one file. After numerous test and
comparisons between attempted encryption by the program and my physical model's verification, a common error arose in
many of the components that were commonly used. Examples would be that rotors that were suppose to complete 
fundamentally the same task functioned differently. By using an iterative process where following these tests, I made
each component a class and transformed the program along the lines of Object Oriented Programming. By revising the 
both the errors decreased due to easier debugging as well as management in complexity and created uniformity between components.

## 2C

```python
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
```

In the block above, the run() method rotates the 3 rotors independently at set times. The rotate motor algorithm, the 
last part of the sequence, checks if rotate() methods returned value which is the current rotation of that rotor returns
the value zero in modulo 26. The if statement occurs for the fastest rotating rotor and then the next rotor in sequential 
speed. Should a rotor rotate, the next fastest rotor will have an identical nested if statement. The selected algorithm 
affects the run() method by changing the permutation of the mono-alphabetic shift.

## 2D

```python
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

```

In the overall program, there are 3 instances of the rotor class to replicate the original machine. Each instance of the
rotor class is required to complete the same actions: the calc() method which calculate the substitution for the letter 
and rotate() method which changes the permutation of the rotor. By creating a class with all duplicated methods helped
manage complexity through code reuse. Rather than having 3 instances of duplicated code where simple typos could result
in hours of debugging, errors and incorrect encryption could be managed by simply visiting this class.
