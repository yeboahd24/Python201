from tkinter import *
from tkinter.messagebox import showinfo
from googletrans import Translator

window = Tk()
window.title("Google Translator")
window.geometry("200x100")


def do_translation():
    word = entry.get()   # this translate the word you specify in the entry box
    results = translator.translate(word).text
    showinfo("Translation", results)


translator = Translator()
label1 = Label(window, text="Enter your word: ")
label1.grid(row=0, column=-0)

entry = Entry(window)
entry.grid(row=1, column=0)

button = Button(window, text="Translate", command=do_translation)
button.grid(row=2, column=0)

window.mainloop()
