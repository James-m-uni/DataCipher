import tkinter as tk
from tkinter import messagebox

from Ciphers import timeCipher
from Ciphers import letterCipher

root = tk.Tk()

timeCipher = timeCipher.timeCipher()
letterCipher = letterCipher.letterCipher()

cipherTypes = [timeCipher, letterCipher]

root.title("Cipher")
welcome = tk.Label(root, text="Welcome to Cipher. Select a cipher option, enter your text then press encode or decode.")
listBox = tk.Listbox(root)

def encrypt(chosenCipher, text):
    for x in cipherTypes:
        if x.getName() == chosenCipher:
            #check if the chosen cipher requires a key
            if x.getRequiresCustomKey():
                pass
            else:
                encryptedMsg = x.encrypt(text)

                #show message to user
                messagebox.showinfo("Encrypted", encryptedMsg)



def decrypt():
    pass

encryptButton = tk.Button(root, text = "encode")


#populate listbox with cipher options
for i in range(0, len(cipherTypes)):
    listBox.insert(i + 1, cipherTypes[i].getName())

text = tk.Entry(root, width=50)

welcome.pack()
listBox.pack()
text.pack()

encrypt("Time Cipher", "This is a test")
root.mainloop()