E N I G M A      M A C H I N E

--INTENDED PURPOSE --

The program will attempt to emulate the german enigma machine used in WW2 in its function that it will encrypt and decipher messages.

The way that it emulates the enigma machine is elaborated upon in the METACODE file, but in brief, an input in the Keyboard function will be encrypted to its location in a standard alphabet. This location will then be scrambled based on settings inputted in the plugboard, to the inputted letter's location on an altered, encrypted alphabet. The location on this alphabet will then be forwarded to a separate, readily defined, altered alphabet on the rotor. The letter has now changed once more. The position of this letter on a standard alphabet will then be forwarded to the next rotor, and so on and so on until it reaches a reflector, which bounces the signal back to the plugboard, and the keyboard, which also acts as a decipherer. 

The rotor(s) can move, which is what adds an added layer of encryption to the enigma machine, but I am not sure I will be able to implement it before the deadline of this project. To that end, I will be satisfied if I can create a program that can encrypt what the user inputs through ONE user altered alphabet (plugboard), then THREE rotors containing a pre-set alphabet. 

--DUE TO TIME CONSTRAINTS --
This enigma machine does not have moving rotors like the actual german enigma machine does. However, it DOES still allow the user to succesfully encrypt and decrypt sentences based on what settings are used in the plugboard, what rotors are used in what order, and the order of the letters in the rotors. This means that a user can encrypt a message, then give the plugboard settings used, and what rotors are used in what order ( there are currently three slots, and five rotor types in the rotor_type file). This would act like a "key" to the encryption just as the codebooks used by the germans. This can be demonstrated by running main.py and alternative_setup.py sequentially, where it is apparent that the same words do not return the same encrypted/decrypted words unless the settings used in the program is identical.

-- LIMITATIONS OF THE CURRENT ITERATIONS OF THE PROGRAM --
As the rotors do not move (YET), it decreases the level of encryption performed by the program. However, even though a BOMBE machine isn't necessary to decipher a message from this version of the program, due to being able to vary what rotor goes where, and even what a rotor contains, there is still a considerable amount of encryption performed.

-- SMALL UPDATES NEEDED --
- Methods in rotor (encrypt) and (decrypt) need to have their names changed - perhaps to (input) and (output) to reflect what they actually do
- catch more errors in input

-- BIG UPDATES NEEDED --
- implement actual rotate function into rotor class based on turning notch
- better design of pipeline class so that it asks used what letters the user would like to change and also what rotors should be placed where


