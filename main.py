from tkinter import *
from console import ConsoleText

from config import CONFIG

def long():
    console.println("LONG")


def short():
    console.println("SHORT")


def exit_long():
    console.println("EXIT LONG")


def exit_short():
    console.println("EXIT SHORT")


def clear():
    console.clear()


if __name__ == "__main__":
    root = Tk()
    root.geometry("500x200")

    BTNs = Frame()
    console = ConsoleText()

    Button(BTNs, width=15, text="LONG", command=long).pack()
    Button(BTNs, width=15, text="EXIT LONG", command=exit_long).pack()
    Button(BTNs, width=15, text="SHORT", command=short).pack()
    Button(BTNs, width=15, text="EXIT SHORT", command=exit_short).pack()

    Button(BTNs, width=15, text="Clear", command=clear).pack(pady=20)

    BTNs.pack(side=LEFT)
    console.pack(side=LEFT)

    root.mainloop()