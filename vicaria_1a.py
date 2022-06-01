from tkinter import *
import sys

class StdoutRedirector(object):
    def __init__(self,text_widget):
        self.text_space = text_widget
        self.text_space.config(bg="black", fg="white", font=("OCR A Extended", 12))
        # self.text_space.config(state=DISABLED)
        self.write("Vicaria AGI interface v1.0.0\nType /help for a list of commands, or ")

    def write(self,string):
        self.text_space.config(state=NORMAL)
        self.text_space.insert(END, string)
        self.text_space.see(END)
        self.text_space.config(state=DISABLED)

    def flush(self):
        pass
        # self.text_space.config(state=NORMAL)
        # self.text_space.delete("1.0", END)
        # self.text_space.config(state=DISABLED)

def processCommand():


window = Tk()
window.title("Vicaria AGI")
text = Text(window)
text.pack()
commandInput = Entry(cw, width=40, bg="black", fg="white", font=("OCR A Extended", 12))
sys.stdout = StdoutRedirector(text)
print("")
window.mainloop()
