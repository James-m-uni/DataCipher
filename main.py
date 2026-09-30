import tkinter as tk

from Ciphers import timeCipher
from Ciphers import letterCipher

root = tk.Tk()

timeCipher = timeCipher.timeCipher()
letterCipher = letterCipher.letterCipher()

cipherTypes = [timeCipher, letterCipher]

root.title("Cipher")
welcome = tk.Label(root, text="Welcome to Cipher. Select a cipher option, enter your text then press encode or decode.")

listBox = tk.Listbox(root)
for i in range(0, len(cipherTypes)):
    listBox.insert(i + 1, cipherTypes[i].getName())

text = tk.Entry(root, width=50)

welcome.pack()
listBox.pack()
text.pack()


root.mainloop()