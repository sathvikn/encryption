import random

class caesarCipher(object):
    alphabet = ['A','B','C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T', 'U','V','W','X','Y','Z']
    def __init__(self, message, shift):
        self.message = message
        self.shift = shift

    def encrypt(self, alphabet):
        encrypted_message = ""
        int_shift = alphabet.index(self.shift)
        for letter in self.message:
            if letter.isalpha():
                stayInAlphabet = ord(letter) + int_shift
                if stayInAlphabet > ord('z'):
                    stayInAlphabet -= 26
                encryptedLetter = chr(stayInAlphabet)
                encrypted_message += encryptedLetter
        return encrypted_message
    def decrypt(self, encrypted,alphabet):
        decryptedMessage = ""
        int_shift = alphabet.index(self.shift)
        for letter in encrypted:
            if letter.isalpha():
                stayInAlphabet = ord(letter) - int_shift
                if stayInAlphabet < ord('a'):
                    stayInAlphabet += 26
            decryptedLetter = chr(stayInAlphabet)
            decryptedMessage += decryptedLetter
        return decryptedMessage



class vigenereCipher(caesarCipher):
    def __init__(self, message, key):
        self.message = message
        new_key = ""
        for c in self.message:
            if len(self.message) - len(key) >= len(new_key):
                new_key += key
            else:
                remainder_length = len(self.message) - len(new_key)
                new_key += new_key[:remainder_length]
        self.key = new_key
    def encryptVig(self):
        encrypted_message = ""
        for mess_char in self.message:
                c = caesarCipher(mess_char, self.key[self.message.index(mess_char)])
                encrypted_message += c.encrypt(caesarCipher.alphabet)
        return encrypted_message

class oneTimePad(object):
    def __init__ (self, message):
        self.message = message

    def encrypt(self):
        key_len = len(self.message)
        key = ""
        for i in range(0, key_len):
            key += random.choice(caesarCipher.alphabet)
            i += 1
        encrypted_message = ""
        for mess_char in self.message:
            c = caesarCipher(mess_char, key[self.message.index(mess_char)])
            encrypted_message += c.encrypt(caesarCipher.alphabet)
        return encrypted_message
run = True
while run == True:
    message = input("Input a message to encrypt (Write \"STOP\" to exit)")
    if message == "STOP":
        run = False
    method = input("How would you like to encrypt the message (input either \"Caesar\", \"Vigenere\" or \"Onetime Pad\")")
    if method == "Caesar":
        c_shift = input("What letter should be \"A\"?")
        c = caesarCipher(message, c_shift)
        print(c.encrypt(c.alphabet))
    if method == "Vigenere":
        v_shift = input("What letter should be \"A\"?")
        v = vigenereCipher(message, v_shift)
        print(v.encryptVig())
    if method == "Onetime Pad":
        o = oneTimePad(message)
        print(o.encrypt())
if run == False:
    print("Terminated")




