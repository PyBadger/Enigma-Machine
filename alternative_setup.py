from set_parts import Keyboard, Plugboard, Rotor, Reflector, Pipeline
from changable_parts import I, II, III, IV, V
from changable_parts import A as refA

kb = Keyboard()
pb = Plugboard("A-D", "E-G", "Y-K") # arg 1, 2 and 3 represent what letters one would like to change on the plugboard

#Choose which rotors to have in what position here, note that the second arg has a placeholder "Q" which is 
#Supposed to represent at what notch the rotor is supposed to turn. That function hasn't been developed 
# yet! 

r1 = Rotor(I, "Q") 
r2 = Rotor(IV, "Q")
r3 = Rotor(II, "Q")
refl = Reflector(refA)

start = Pipeline(kb, pb,r1,r2,r3,refl)


