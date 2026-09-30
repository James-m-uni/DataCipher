#uses a single ascii character turned into binary and added to each character of the text to be encoded

class letterCipher:
    def __init__(self):
        self.name = "Letter Cipher"
        self.requiresCustomKey = True

    def getName(self):
        return self.name

    def getRequiresCustomKey(self):
        return self.requiresCustomKey

    def encrypt(self, plainText, customKey):
        pass

    def decrypt(self, cipherText, customKey):
        pass