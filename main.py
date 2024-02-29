from keyboard import Keyboard 
from plugboard import Plugboard 


k = Keyboard()
print(k.encrypt("A"))
print(k.decrypt(0))

A = k.encrypt("A")

p = Plugboard("A-D", "D-C", "Z-E")
print(p.encrypt(A))
p.print_encrypted()
#Encryption, so far so good

c= p.decrypt(3)
print(k.decrypt(c))
#Decryption, so far so good.