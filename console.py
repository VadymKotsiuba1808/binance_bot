from tkinter import *

class ConsoleText(Text):

    def clear(self):
        self.delete(0.0, END)

    def print(self, data: str):
        self.insert(END, data)

    def println(self, data: str):
        self.insert(END, data+'\n')