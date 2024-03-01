from set_parts import Keyboard, Plugboard, Rotor, Reflector, Pipeline
from changable_parts import I, II, III, IV, V
from changable_parts import A as refA

kb = Keyboard()
pb = Plugboard("A-D", "E-G", "Y-K")
r1 = Rotor(I, "Q")
r2 = Rotor(II, "Q")
r3 = Rotor(III, "Q")
refl = Reflector(refA)

start = Pipeline(kb, pb,r1,r2,r3,refl)


