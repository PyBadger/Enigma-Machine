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
        pairsofletters = [self.pairA, self.pairB, self.pairC] # letters with "-""
        self.pairsofletters_clean = [] #container for letters once formatted
        
        
        

        #removes "-"" from input
        for pair in pairsofletters:
            pair = pair.split("-")
            self.pairsofletters_clean.append(pair) 
        #Triggers the letters to be changed
        self.changeletters()
        

        

            
    def changeletters(self):
        for letter in self.pairsofletters_clean:
            first = letter[0]
            second = letter[1]
            #finds position of letter in the alphabet to be encrypted
            pos_first = self.enc_alph.find(first) 
            pos_second = self.enc_alph.find(second)
            #cuts encrypted alphabet just before the pos of the letter that we want to replace, adds the
            # letter we want there, then adds the remainder of the alphabet
            self.enc_alph = self.enc_alph[:pos_first]+second+self.enc_alph[pos_first+1:]
            self.enc_alph = self.enc_alph[:pos_second]+first+self.enc_alph[pos_second+1:]

    def print_encrypted(self):
        #This is just a troubleshooting method
        print(self.stand_alph)
        print(self.enc_alph)
    
    

            
        

"""For Troubleshooting """
#p = Plugboard("A-B", "D-C", "Z-E")
#p.print_encrypted()


    
    