

class Reflector:
    def __init__(self, type):
        """ This acts like a rotor, but without any possibility to alter the order of the alphabet, the position that it
        forwards is then sent backwards"""
        self.stand_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.enc_alph = type #This represents rotor type and also what will then be the encrypted alphabet
    def reflect(self, pos):
            #Takes position from previous rotor and gives the letter that it corresponds to on the new encrypted alphabet
            #it then gives the position that THAT letter is found on a standard alphabet, and sentds it back to the rotor.
            letter = self.enc_alph[pos] #returns letter which the position corresponds to
            pos_stand = self.stand_alph.find(letter) #finds position of the letter in standard_alph.
            return pos_stand #returns the position of the letter in the encrypted alphabet
    def print_alph(self):
          #This is just for troubleshooting
          print(self.enc_alph, "--This is the scrambled alphabet")
          print(self.stand_alph, "-This is the standard alphabet")  
    