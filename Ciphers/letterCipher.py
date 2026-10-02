#uses a single ascii character turned into its numeric ascii version * the numeric ascii of the key

class letterCipher:
    def __init__(self):
        self.name = "Letter Cipher"
        self.requiresCustomKey = True

    def getName(self):
        return self.name

    def getRequiresCustomKey(self):
        return self.requiresCustomKey

    def encrypt(self, plainText, customKey : str):
        encryptedText = ""
        for i in range(0, len(plainText)):
            newChar = chr(ord(plainText[i]) * ord(customKey))
            encryptedText += newChar
            print(encryptedText)
        return encryptedText

    def decrypt(self, cipherText, customKey):
        decryptedText = ""
        for i in range(0, len(cipherText)):
            newChar = chr(ord(cipherText[i]) // ord(customKey))
            decryptedText += newChar
        return decryptedText