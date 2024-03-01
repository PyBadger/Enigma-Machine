
class Rotor:
    def __init__(self, type, tnotch):
        """This class will take a letter, encrypt it, and then move the alphabet in which it was encrypted
        one step forward (ABC becomes BCD, for example). The encrypted alphabet it uses will depend on the 
        rotor type inputted (I-III), which is the first level of encryption deployed. Furthermore, once the 
        alphabet has moved to a certain point (tnotch) it will signal the consequetive rotor( and its alphabet )
        to move one step forward."""

        """NOTE! I will first introduce the new, scrambled alphabet, and make sure that the encryption and decr
         yption can move to and from the plugboard to the reflector. THEN I will try to implement the actual rotation 
          mechanism.. Somehow. """ 

        self.tnotch = tnotch #This is the turnover notch, which represents the letter at which the rotor will
                            # Cause the other rotor to turn one step.
        self.stand_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.enc_alph = type #This represents rotor type and also what will then be the encrypted alphabet
    def encrypt(self, pos):
            #Gives corresponding position of the letter that has passed from the plugboard or the previous rotor
            #Which is the value which will be used in the next rotor to encrypt your letter further.
            letter = self.stand_alph[pos] #returns letter which the position corresponds to
            pos_encr = self.enc_alph.find(letter) #finds position of the letter in encrypted alphabet.
            return pos_encr #returns the position of the letter in the encrypted alphabet
    def decrypt(self, pos):
            #The rotor transfers the position, which is then decrypted back into the position of original alphabet
            pos_encr = self.enc_alph[pos] #What letter is at the position the rotor will give us
            pos_decr = self.stand_alph.find(pos_encr) #where is this letter in the unscrambled alphabet
            return pos_decr #this can then be fed into keyboard to give the letter back    
    def print_alph(self):
          #This is just for troubleshooting
          print(self.enc_alph, "--This is the scrambled alphabet")
          print(self.stand_alph, "-This is the standard alphabet")        



      