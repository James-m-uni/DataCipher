import tkinter as tk
from tkinter import messagebox
from tkinter.constants import ACTIVE

from Ciphers import timeCipher
from Ciphers import letterCipher

root = tk.Tk()

timeCipher = timeCipher.timeCipher()
letterCipher = letterCipher.letterCipher()

cipherTypes = [timeCipher, letterCipher]

root.title("Cipher")
welcome = tk.Label(root, text="Welcome to Cipher. Select a cipher option, enter your text then press encode or decode.")
listBox = tk.Listbox(root)

def encrypt(chosenCipher, textToEncrypt):
    for x in cipherTypes:
        if x.getName() == chosenCipher:
            #check if the chosen cipher requires a key
            if x.getRequiresCustomKey():
                key = ""

                keyWindow = tk.Tk()
                keyWindow.title("Enter encryption key")
                keyEntryBox = tk.Entry(keyWindow)

                def getKeyAndEncrypt():
                    key = keyEntryBox.get()
                    keyWindow.destroy()
                    encryptedMsg = x.encrypt(textToEncrypt, key)
                    messagebox.showinfo("Encrypted Text", encryptedMsg)

                continueButton = tk.Button(keyWindow, text="Confirm key", command=lambda: getKeyAndEncrypt())

                keyEntryBox.pack()
                continueButton.pack()

                keyWindow.mainloop()




            else:
                encryptedMsg = x.encrypt(textToEncrypt)

                #show message to user
                messagebox.showinfo("Encrypted", encryptedMsg)
                return



def decrypt(chosenCipher, textToDecrypt):
    for x in cipherTypes:
        if x.getName() == chosenCipher:
            #check if the chosen cipher requires a key
            if x.getRequiresCustomKey():
                if x.getRequiresCustomKey():
                    key = ""

                    keyWindow = tk.Tk()
                    keyWindow.title("Enter encryption key")
                    keyEntryBox = tk.Entry(keyWindow)

                    def getKeyAndUnencrypt():
                        key = keyEntryBox.get()
                        keyWindow.destroy()
                        encryptedMsg = x.decrypt(textToDecrypt, key)
                        messagebox.showinfo("Decrypted Text", encryptedMsg)

                    continueButton = tk.Button(keyWindow, text="Confirm key", command=lambda: getKeyAndUnencrypt())

                    keyEntryBox.pack()
                    continueButton.pack()

                    keyWindow.mainloop()




            else:
                unencryptedMsg = x.decrypt(textToDecrypt)

                #show message to user
                messagebox.showinfo("Unencrypted", unencryptedMsg)
                return

text = tk.Entry(root, width=50)
encryptButton = tk.Button(root, text = "encode", command = lambda: encrypt(listBox.get(ACTIVE), text.get()))
decryptButton = tk.Button(root, text = "decode", command = lambda: decrypt(listBox.get(ACTIVE), text.get()))



#populate listbox with cipher options
for i in range(0, len(cipherTypes)):
    listBox.insert(i + 1, cipherTypes[i].getName())

welcome.pack()
listBox.pack()
text.pack()
encryptButton.pack()
decryptButton.pack()
root.mainloop()