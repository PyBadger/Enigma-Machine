"""""
This finds the numerical position of an inputted letter in the alphabet, and can also return the letter based on
the numerical position given
"""

class Keyboard:
    def encrypt(self, inpletter):
        #finds position in the alphabet
        pos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(inpletter)
        return pos
    def decrypt(self, pos):
        #finds letter based on position
        outpletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[pos]
        return outpletter

