from tkinter import *
from console import ConsoleText

import logging
from binance.cm_futures import CMFutures as Client
from binance.lib.utils import config_logging
from binance.error import ClientError

from config import CONFIG

config_logging(logging, logging.DEBUG)

binance_client = Client(CONFIG.key, CONFIG.secret, base_url="https://fapi.binance.com")
binance_client.change_leverage(CONFIG.ticker, CONFIG.leverage)

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