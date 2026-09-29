import tkinter as tk

root = tk.Tk()

cipherTypes = []

root.title("Cipher")
root.geometry("500x500")
welcome = tk.Label(root, text="Welcome to Cipher. Select a cipher option, enter your text then press encode.")

listBox = tk.Listbox(root)
for i in cipherTypes:
    listBox.insert(i, cipherTypes[i].getName)


from Ciphers import timeCipher

test = timeCipher.timeCipher()
print(test.encrypt("This is a test of the time cipher"))


text = tk.Entry(root, width=50)

welcome.pack()
text.pack()


root.mainloop()