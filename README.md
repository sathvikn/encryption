A short summer project when I decided to implement several ciphers described in Simon Singh's The Code Book into Python.
It works using a command-line interface where the user selects their preferred method of encryption, a message to encrypt,
and if necessary, a key. 

I created three cipher objects whose attributes were a list of the characters in the alphabet and a string representing a message
The key of the Caesar cipher is a letter of the alphabet, the cipher text is obtained from letting the key serve as "A," the
letter after as "B," and so forth.

The key of the Vigenère cipher is a series of letters. Encryption is performed by matching each letter in the key to a letter
in a message and encrypting that particular letter using the Caesar cipher from its corresponding letter in the key.

The onetime pad cipher works similarly to the Vigenère cipher, but uses a randomly generated key that is the length of the message.
As a result, it is theoretically unbreakable (the first two ciphers I implemented were both broken centuries ago).
