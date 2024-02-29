Enigma machine

Intended purpose:
The program will attempt to emulate the german enigma machine used in WW2 in its function that it will encrypt and decipher messages.

The way that it emulates the enigma machine is elaborated upon in the METACODE file, but in brief, an input in the Keyboard function will be encrypted to its location in a standard alphabet. This location will then be scrambled based on settings inputted in the plugboard, to the inputted letter's location on an altered, encrypted alphabet. The location on this alphabet will then be forwarded to a separate, readily defined, altered alphabet on the rotor. The letter has now changed once more. The position of this letter on a standard alphabet will then be forwarded to the next rotor, and so on and so on until it reaches a reflector, which bounces the signal back to the plugboard, and the keyboard, which also acts as a decipherer. 

The rotor(s) can move, which is what adds an added layer of encryption to the enigma machine, but I am not sure I will be able to implement it before the deadline of this project. To that end, I will be satisfied if I can create a program that can encrypt what the user inputs through ONE user altered alphabet (plugboard), then THREE rotors containing a pre-set alphabet. 

*b If there is even more time
- I will try to create a GUI that projects the user input in real time, much like the lamp-board (?) did in real life.