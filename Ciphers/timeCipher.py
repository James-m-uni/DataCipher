import datetime

#this cipher gets the current date and multiplies them to create a big number. The ascii base 10 number of each letter is then taken away with the remainder being substituted

class timeCipher(object):
    def __init__(self):
        self.name = "timeCipher"


    def getName(self):
        return self.name

    def encrypt(self, text):
        encryptedText = ""

        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day

        key = year*month*day

        for i in range (1,len(text)):
            encryptedCharNum = key - ord(text[i])
            length = len(str(encryptedCharNum))
            encryptedText += str(length) + str(encryptedCharNum)

        return encryptedText

