# Enigma

The program was written in python. The purpose of this program is to demonstrate encryption by an Enigma Machine. The 
program takes an input string and proceeds to run a 3-motor enigma machine encryption. The encryption is poly-alphabetic 
as after the encryption of a letter, one or more rotor rotates a step causing the permutation of the alphabet to 
change. The encryption by rotor is one-way and does not encrypt the same in both directions. A letter is 
encrypted in the following path: input -> plugboard -> rotor 1 -> rotor 2 -> rotor 3 -> reflector -> rotor 3 -> rotor 2 
-> rotor 1 -> plugboard -> output. Per encryption of a letter, rotor 1 rotates. When a rotor 'n' completes 26 rotations,
rotor 'n+1' rotates a step. The video shows the encryption and decryption of the phrase 'hello world'. When run, the 
following information will be printed: all rotor permutations of the alphabet and the plugboard substitutions.

## Getting Started
1. Download/Clone Repository
2. Navigate to `../Enigma/`
3. Run `pip install -r requirements.txt`
4. Navigate to `../Enigma/Python/`
5. To begin, run the following command: `python enigma.py`


### Prerequisites
* [Python 3](https://www.python.org/)
* [Numpy](https://pypi.org/project/numpy/)
* [Pyfiglet](https://pypi.org/project/pyfiglet/)
* [PyInquirer](https://pypi.org/project/PyInquirer/)

### How to Use

When you first run the program, you will be prompted to either create an enigma machine with custom or random settings. Custom settings allow for customization of the permutation on each rotor as well as the starting position on each rotor while random settings creates a completely random permutation and starting position for the rotors. After the prompts are completed, the enigma key will be displayed as well as a prompt for text to encrypt/decrypt.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Dr. David Perry, National Security Agency
