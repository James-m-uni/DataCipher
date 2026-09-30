import datetime

#this cipher gets the current date and multiplies them to create a big number. The ascii base 10 number of each letter is then taken away with the remainder being substituted

class timeCipher(object):
    def __init__(self):
        self.name = "Time Cipher"
        self.requiresCustomKey = False

    def getRequiresCustomKey(self):
        return self.requiresCustomKey

    def getName(self):
        return self.name

    def encrypt(self, text):
        encryptedText = ""

        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day

        key = year*month*day

        for i in range (0,len(text)):
            encryptedCharNum = key - ord(text[i])
            length = len(str(encryptedCharNum))
            encryptedText += str(length) + str(encryptedCharNum)

        return encryptedText

    def decrypt(self, text):
        decryptedText = ""

        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day

        key = year*month*day

        finished = False
        currentIndex = 0

        while not finished:
            #find the length of the next phrase to decode
            phraseLength = int(text[currentIndex])

            phrase = ""

            #get each character in the phrase
            for i in range(1, phraseLength + 1):
                phrase += text[currentIndex+i]

            #update the index ready for the next phrase
            currentIndex += phraseLength + 1

            #decode the phrase using the unique day key
            decryptedCharNum = key - int(phrase)

            decryptedText += chr(decryptedCharNum)

            if currentIndex == len(text):
                finished = True


        return decryptedText
