#Rotor types
I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

# sourced from https://en.wikipedia.org/wiki/Enigma_rotor_details

class Rotor:
    def __init__(self, type, tnotch):
        """This class will take a letter, encrypt it, and then move the alphabet in which it was encrypted
        one step forward (ABC becomes BCD, for example). The encrypted alphabet it uses will depend on the 
        rotor type inputted (I-III), which is the first level of encryption deployed. Furthermore, once the 
        alphabet has moved to a certain point (tnotch) it will signal the consequetive rotor( and its alphabet )
        to move one step forward."""

        """NOTE! I will first introduce the new, scrambled alphabet, and make sure that the encryption and decr
         yption can move from the plugboard to the reflector. THEN I will try to implement the actual rotation 
          mechanism.. Somehow. """ 

        self.tnotch = tnotch #This is the turnover notch, which represents the letter at which the rotor will
                            # Cause the other rotor to turn one step.
        self.stand_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.enc_alph = type #This represents rotor type and also what will then be the encrypted alphabet

    
