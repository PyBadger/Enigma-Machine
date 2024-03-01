from keyboard import Keyboard 
from plugboard import Plugboard 
from rotor import Rotor
from rotor_types import I, II, III
from rotor_types import A as refA
from reflector import Reflector

#I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

k = Keyboard()
print(k.encrypt("P"))
#print(k.decrypt(0))

#Letter A is now position 0 on the alphabet
A = k.encrypt("A")

p = Plugboard("A-D", "D-C", "Z-E")
#Position A and D has been replaced, so A should be scrambled into position 3

print(p.encrypt(A))
p.print_encrypted()
#Encryption, so far so good

c= p.decrypt(3)
print(k.decrypt(c))
#Decryption, so far so good.

rotorI = Rotor(I, "Q")

print(rotorI.encrypt(3))
#Position 3 in rotor I is currently G, which on the standardized alphabet is position 6
rotorI.print_alph()
rotorII = Rotor(II, "V")
print(rotorII.encrypt(6))
rotorII.print_alph()

ref = Reflector(refA)
print(ref.reflect(17))
ref.print_alph()
#Becomes N in the standard alphabet, and is fed back into the rotor system

print(rotorII.decrypt(13))
rotorII.print_alph()
print(rotorI.decrypt(19))
print(p.decrypt(15))
print(k.decrypt(15))