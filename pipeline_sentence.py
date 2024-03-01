from keyboard import Keyboard 
from plugboard import Plugboard 
from rotor import Rotor
from rotor_types import I, II, III
from rotor_types import A as refA
from reflector import Reflector

kb = Keyboard()
pb = Plugboard("A-D", "D-C", "Z-E")
rotorI = Rotor(I, "Q")
rotorII = Rotor(II, "Q")
rotorIII = Rotor(III, "Q")
ref = Reflector(refA)

class Pipeline:
    def __init__(self):
        self.sentence = input("Enter sentence, please ")
        self.underscore = self.sentence.replace(" ", "_") #replaces empty space with underscore
        self.chunks = self.underscore.split() #creates chunks of words out of the sentences
        self.repo = [] #A repository to store the encrypted letters
        self.encrypted_sentence = "ABCD" #placeholder
        self.process()
        self.form_sentence()
        print("You wrote:", self.sentence)
        print("That is encrypted into: ", self.encrypted_sentence)
    
    def cleanup(self):
        

    def process(self):
        for word in self.chunks:
            for letter in word:
                if letter == "_":
                    self.repo.append("_")  #If there's a space used in the sentence, just add it to the repo, and continue loop
                    continue
                enc_kb = kb.encrypt(letter)
                enc_pb = pb.encrypt(enc_kb)
                enc_rI = rotorI.encrypt(enc_pb)
                enc_rII = rotorII.encrypt(enc_rI)
                enc_rIII = rotorIII.encrypt(enc_rII)
                re = ref.reflect(enc_rIII)
                enc_rIII = rotorIII.decrypt(re)
                enc_rII = rotorII.decrypt(enc_rIII)
                enc_rI = rotorI.decrypt(enc_rII)
                enc_pb = pb.decrypt(enc_rI)
                enc_kb = kb.decrypt(enc_pb)
                self.repo.append(enc_kb)
    def form_sentence(self):
        self.encrypted_sentence = "".join(self.repo) #puts the letters together from the repository
        self.encrypted_sentence = self.encrypted_sentence.replace("_", " ") #replaces the "_" we've added with spaces
       

            
        


           



b = Pipeline()
#b.process()
#b.form_sentence()