from .keyboard import Keyboard 
from .plugboard import Plugboard 
from .rotor import Rotor
from .reflector import Reflector


class Pipeline:
    def __init__(self, keyboard, plugboard, rotator1, rotator2, rotator3, reflector):
        self.kb = keyboard #keyboard
        self.pb = plugboard #plugboard
        self.rI = rotator1 #First Rotor
        self.rII = rotator2#Second Rotor
        self.rIII = rotator3 #Third Rotor
        self.ref = reflector #Reflector

        self.sentence = input("Enter sentence, \n.. and do not use any strange symbols or letters than what is contained in a standard english alphabet: ")
        self.cleanup()
        self.chunks = self.underscore.split() #creates chunks of words out of the sentences
        self.repo = [] #A repository to store the encrypted letters
        self.encrypted_sentence = "ABCD" #placeholder
        self.process()
        self.form_sentence()
        print("You wrote:", self.sentence)
        print("That is encrypted into: ", self.encrypted_sentence)
        
    def cleanup(self):
        self.sentence = self.sentence.upper() #Ensures all letters are in caps
        self.underscore = self.sentence.replace(" ", "_") #replaces empty space with underscore

    def process(self):
        for word in self.chunks:
            for letter in word:
                if letter == "_":
                    self.repo.append("_")  #If there's a space used in the sentence, just add it to the repo, and continue loop
                    continue
                enc_kb = self.kb.encrypt(letter)
                enc_pb = self.pb.encrypt(enc_kb)
                enc_rI = self.rI.encrypt(enc_pb)
                enc_rII = self.rII.encrypt(enc_rI)
                enc_rIII = self.rIII.encrypt(enc_rII)
                reflctr = self.ref.reflect(enc_rIII)
                enc_rIII = self.rIII.decrypt(reflctr)
                enc_rII = self.rII.decrypt(enc_rIII)
                enc_rI = self.rI.decrypt(enc_rII)
                enc_pb = self.pb.decrypt(enc_rI)
                enc_kb = self.kb.decrypt(enc_pb)
                self.repo.append(enc_kb)
    def form_sentence(self):
        self.encrypted_sentence = "".join(self.repo) #puts the letters together from the repository
        self.encrypted_sentence = self.encrypted_sentence.replace("_", " ") #replaces the "_" we've added with spaces
       

            
        


           

