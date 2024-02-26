"""
This class acts as the first line of encryption, allowing the user to change the position of three letters
from the standardized alphabet stand_alph to an encrypted alphabet enc_alph"""

class Plugboard:

    def __init__(self, pairA, pairB, pairC):
        #change_letters will be in the format of A-B, assume its all been capitalized
        self.stand_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.enc_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #before its encrypted/changed through the plugboard
        self.pairA = pairA
        self.pairB = pairB
        self.pairC = pairC
        self.pairsofletters = [self.pairA, self.pairB, self.pairC]

        #removes - from input
        for pair in self.pairsofletters:
            pair = pair.split("-")

            
        self.clean_letters = inp_letters.split("-")
        self.letter1 = self.clean_letters[0]
        self.letter2 = self.clean_letters[1]
        self.pos_letter1 = self.enc_alph.find(self.letter1)
        self.pos_letter2 = self.enc_alph.find(self.letter2)
    def changeletters(self):
        #This function produces a new encrypted alphabet based on the letter changes made by the user


p = Plugboard("A-B")

p.changeletters()


    
    